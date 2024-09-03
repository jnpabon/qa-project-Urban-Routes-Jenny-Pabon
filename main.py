from TestUrbanRoutes import TestUrbanRoutes

if __name__ == '__main__':

    # test 1: set the rout
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_set_route()
    tests_urban_routes.teardown_class()

    # test 2: set conform taxi
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_conform_taxi_active()
    tests_urban_routes.teardown_class()

    # test 3: fill or set phone number
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_set_phone_number()
    tests_urban_routes.teardown_class()

    # test 4: fill or set card as payment method
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_set_payment_method()
    tests_urban_routes.teardown_class()

    # test 5: fill or set a comment to the driver
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_set_comment()
    tests_urban_routes.teardown_class()

    # test 6: select blanket and scarves
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_set_blanket_and_scarves()
    tests_urban_routes.teardown_class()

    # test 7: order 2 ice cream
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_set_ice_cream()
    tests_urban_routes.teardown_class()

    # test 8: order taxi
    tests_urban_routes = TestUrbanRoutes()
    tests_urban_routes.setup_class()
    tests_urban_routes.test_order_conform_taxi_active()
    tests_urban_routes.teardown_class()
