import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None
    urban_routes_home_page = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.urban_routes_home_page = UrbanRoutesPage(cls.driver)
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        urban_routes_home_page = self.urban_routes_home_page
        address_from = data.address_from
        address_to = data.address_to
        urban_routes_home_page.set_route(address_from, address_to)

    def test_conform_taxi_active(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()

    def test_set_phone_number(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()
        urban_routes_home_page.set_phone_number()

    def test_set_payment_method(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()
        urban_routes_home_page.set_card_as_payment_method()

    def test_set_comment(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()
        urban_routes_home_page.set_comment()

    def test_set_blanket_and_scarves(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()
        urban_routes_home_page.set_blanket_and_scarves()

    def test_set_ice_cream(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()
        urban_routes_home_page.set_ice_cream()

    def test_order_conform_taxi_active(self):
        urban_routes_home_page = self.urban_routes_home_page
        urban_routes_home_page.order_conform_taxi_option()
        urban_routes_home_page.set_phone_number()
        urban_routes_home_page.set_card_as_payment_method()
        urban_routes_home_page.set_comment()
        urban_routes_home_page.set_blanket_and_scarves()
        urban_routes_home_page.set_ice_cream()
        urban_routes_home_page.modal_taxi_search()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
