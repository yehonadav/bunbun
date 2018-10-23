from qaviton.locator import Locator


class locator(Locator):
    # you can use a variety of methods to build locators
    welcome_to_flask_app = ("text", "Welcome To FlaskApp")
    lead = (('class', 'lead'), ('text', 'This application is built with Python Flask framework'))
    login = (('href', '/login'), ('class', 'btn btn-success btn-lg'))
    register = (('href', '/register'), ('class', 'btn btn-primary btn-lg'))
    my_flask_app = (('text', 'MyFlaskApp'), ('class', 'navbar-brand'))
    Home = ('text', 'Home')
    About = ('text', 'About')
    Articles = ('text', 'Articles')
    Register = ('text', 'Register')
    Login = ('text', 'Login')

