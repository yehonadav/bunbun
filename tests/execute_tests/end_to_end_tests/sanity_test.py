def test_HomePage_sanity(app):
    """test all elements are found on the page"""
    app.navigate(app.home)
    app.home.About_element()
    app.home.Articles_element()
    app.home.Home_element()
    app.home.Login_element()
    app.home.Register_element()
    app.home.lead_element()
    app.home.login_element()
    app.home.register_element()
    app.home.my_flask_app_element()
    app.home.welcome_to_flask_app_element()
