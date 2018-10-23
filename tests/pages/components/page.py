from qaviton.page import Page as page


class Page(page):
    """component with common behavior to all pages & components alike.
    all of your pages & components should inherit from this common page.

    you should always include here a navigation to your initial login page(starting point)
    so that dependent tests could always start fresh if needed.
    """
    def navigate_to_HomePage(self, weight=10, *args, **kwargs):
        self.driver.get("http://127.0.0.1:5000/")
        self.wait_until_page_loads()
