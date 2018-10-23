import pytest
from tests.services.app import App
from tests.parameters.supported_platforms import platforms


@pytest.fixture(scope='session', params=platforms.get())
def app(request):
    """fixture for cross-platform model-based application
    always use session scope for this type of fixture & parameterize your platforms
    :rtype: App
    """
    if isinstance(request.param, list) or isinstance(request.param, tuple):
        APPS = []
        for platform in request.param:
            APPS.append(App.from_platform(platform, request))
            request.addfinalizer(APPS[-1].driver.quit)
        return APPS
    APP = App.from_platform(request.param, request)
    request.addfinalizer(APP.driver.quit)
    return APP


@pytest.fixture(scope='session', params=platforms.get())
def app2(request):
    """you can use multiple apps or even the same app with different driver sessions in your tests
    :rtype: App
    """
    if isinstance(request.param, list) or isinstance(request.param, tuple):
        APPS = []
        for platform in request.param:
            APPS.append(App.from_platform(platform, request))
            request.addfinalizer(APPS[-1].driver.quit)
        return APPS
    APP = App.from_platform(request.param, request)
    request.addfinalizer(APP.driver.quit)
    return APP
