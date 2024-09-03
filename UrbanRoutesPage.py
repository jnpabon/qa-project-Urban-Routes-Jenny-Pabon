import data
from helperClases.actions import Actions
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    actions = Actions

    # Elments into the homPage
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Elements into the transport picker options
    type_picker_shown = (By.CSS_SELECTOR, '.type-picker.shown')
    mode_container = (By.CSS_SELECTOR, '.mode.active')
    type_active_disabled = (By.CSS_SELECTOR, "div[class='type active disabled'] img[class='type-icon']")
    results_image = (By.CLASS_NAME, 'results-image')
    button_order_taxi_type_picker = (By.XPATH, "//button[normalize-space()='Pedir un taxi']")

    # Elements into the tariff picker options
    tariff_picker_shown = (By.XPATH, "//div[@class='tariff-picker shown']")
    comfort_option = (By.XPATH, "//div[@class='tcard-icon']//img[@alt='Comfort']")
    phone_input = (By.CLASS_NAME, 'np-text')
    pay_button = (By.CLASS_NAME, 'pp-button')
    pay_method_selected = (By.CLASS_NAME, 'pp-value-text')
    comment_input = (By.ID, 'comment')
    blanket_and_scarves_checkbox = (By.XPATH, "//div[@class='workflow']//div[1]//div[1]//div[2]//div[1]//span[1]")
    blanket_and_scarves_checkbox_selected = (By.XPATH,
                                             "//div[normalize-space()='Manta y pañuelos']//input[@class='switch-input']"
                                             )
    ice_cream_counter_plus = (By.XPATH, "//div[@class='r-group']//div[1]//div[1]//div[2]//div[1]//div[3]")
    ice_cream_counter = (By.XPATH, "//div[@class='r-group']//div[1]//div[1]//div[2]//div[1]//div[2]")
    order_taxi_comfort = (By.XPATH, "//button[@class='smart-button']")

    # Pop-up phone number
    phone_number_title_popup = (By.CLASS_NAME, 'head')
    phone_number_input_popup = (By.ID, 'phone')
    phone_number_submit_button_popup = (By.XPATH, "//button[normalize-space()='Siguiente']")
    phone_number_close_button_popup = (By.XPATH,
                                       "//div[@class='number-picker open']//div[@class='section active']//button["
                                       "@class='close-button section-close']")
    phone_number_error_message_popup = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]')

    # Pop-up phone number validation SMS
    phone_number_validation_sms_title_popup = (By.CLASS_NAME, 'head')
    phone_number_validation_sms_code_input_popup = (By.ID, 'code')
    phone_number_validation_sms_confirm_button_popup = (By.XPATH, "//button[normalize-space()='Confirmar']")
    phone_number_validation_sms_send_code_again_button_popup = (By.XPATH, "//button[normalize-space()='Vuelve a "
                                                                          "enviar el código']")
    phone_number_validation_sms_close_button_popup = (By.XPATH, "//div[@class='number-picker open']//div["
                                                                "@class='section active']//button["
                                                                "@class='close-button section-close']")

    # Pop-up pay method
    pay_method_title_popup = (By.CLASS_NAME, 'head')
    pay_method_cash_checkbox_popup = (By.ID, 'cash')
    pay_method_card1_checkbox_popup = (By.ID, 'card-1')
    pay_method_add_card_popup = (By.XPATH, "//div[@class='pp-title'][normalize-space()='Agregar tarjeta']")
    pay_method_close_button_popup = (By.XPATH, "//div[@class='payment-picker open']//div[@class='section "
                                               "active']//button[@class='close-button section-close']")

    # Pop-up add card
    add_card_title_popup = (By.CLASS_NAME, 'head')
    add_card_number_popup = (By.ID, 'number')
    add_card_code_popup = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    add_card_submit_button_popup = (By.XPATH, "//button[normalize-space()='Agregar']")
    add_card_cancel_button_popup = (By.XPATH, "//button[normalize-space()='Cancelar']")
    add_card_close_button_popup = (By.XPATH,
                                   "//div[@class='number-picker open']//div[@class='section active']//button["
                                   "@class='close-button section-close']")

    # modal de busqueda de taxi
    # -----------------localizador cambiado de XPATH a CSS_SELECTOR-----------------------------------------
    modal_searching_taxi = (By.CSS_SELECTOR, 'div.order.shown > div.order-body')
    modal_searching_taxi_title = (By.CSS_SELECTOR,
                                  'div.order.shown > div.order-body > div.order-header > div > div.order-header-title')
    modal_searching_taxi_time = (By.CSS_SELECTOR,
                                 'div.order.shown > div.order-body > div.order-header > div > div.order-header-time')
    modal_searching_taxi_cancel_button = (By.CSS_SELECTOR,
                                          'div.order.shown > div.order-body > div.order-subbody > '
                                          'div.order-buttons > div:nth-child(1) > button')
    modal_searching_taxi_details_button = (By.CSS_SELECTOR, 'div.order.shown > div.order-body > div.order-subbody > '
                                                            'div.order-buttons > div:nth-child(2) > button')
    modal_searching_taxi_pickup_location = (By.CSS_SELECTOR,
                                            'div.order.shown > div.order-body > div.order-subbody > div.order-details '
                                            '> div:nth-child(1) > div.order-details-content > div.o-d-h')
    modal_searching_taxi_destination_address = (By.CSS_SELECTOR,
                                                'div.order.shown > div.order-body > div.order-subbody > '
                                                'div.order-details > div:nth-child(2) > div.order-details-content > '
                                                'div.o-d-h')
    modal_searching_taxi_payment_method = (By.CSS_SELECTOR,
                                           'div.order.shown > div.order-body > div.order-subbody > div.order-details '
                                           '> div:nth-child(3) > div.order-details-content > div.o-d-h')
    modal_searching_taxi_more_information = (By.CSS_SELECTOR,
                                             'div.order.shown > div.order-body > div.order-subbody > '
                                             'div.order-details > div:nth-child(4) > div.order-details-content > '
                                             'div.o-d-h')
    # -----------------localizador cambiado de XPATH a CSS_SELECTOR-----------------------------------------

    # Texts
    flash_mode_text = 'Flash'
    # type of payment methods
    cash_text = 'Efectivo'
    card_text = 'Tarjeta'
    # Texts of order taxi button
    order_button_text = 'Introducir un número de teléfono y reservar'
    order_button_with_phone_number_text = 'Pedir un taxi'
    # Texts of searching taxi modal
    modal_searching_taxi_title_text = 'Buscar automóvil'
    # attributes
    value = 'value'
    src = 'src'

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

# Set from address
    def set_from(self, from_address):
        self.actions.set_input_text(self.from_field, from_address)

# Set to address
    def set_to(self, to_address):
        self.actions.set_input_text(self.to_field, to_address)

# Get the text of from field
    def get_from(self):
        return self.actions.get_property_text(self.from_field, self.value)

    # Get the text of to field
    def get_to(self):
        return self.actions.get_property_text(self.to_field, self.value)

# Wait for load home page
    def wait_for_load_home_page(self):
        self.actions.wait_visibility_of_element_located(self.to_field, 20)

# Wait for load the image of type results
    def wait_for_load_type_results_image(self):
        self.actions.wait_visibility_of_element_located(self.results_image, 10)

# Get the text of the active option
    def get_type_active_disabled(self):
        return self.actions.get_property_text(self.type_active_disabled, self.src)

# Click on button order taxi
    def click_button_order_taxi(self):
        self.actions.click(self.button_order_taxi_type_picker)

# Wait for load the tariff picker shown
    def wait_for_load_tariff_picker_shown(self):
        self.actions.wait_visibility_of_element_located(self.tariff_picker_shown, 10)

# Set the route
    def set_route(self, address_from, address_to):
        actions = self.actions
        self.wait_for_load_home_page()
        self.set_from(address_from)
        self.set_to(address_to)
        self.wait_for_load_type_results_image()
        actions.assert_property_text(self.from_field, self.value, address_from)
        actions.assert_property_text(self.to_field, self.value, address_to)

# Select conform option as type option
    def select_comfort_option(self):
        actions = self.actions
        actions.click(self.comfort_option)

# Click on button to get taxi type conform
    def order_conform_taxi_option(self):
        actions = self.actions
        address_from = data.address_from
        address_to = data.address_to
        self.set_route(address_from, address_to)
        actions.assert_input_text(self.mode_container, self.flash_mode_text)
        actions.assert_text_in_text('taxi-active', self.get_type_active_disabled())
        self.click_button_order_taxi()
        self.wait_for_load_tariff_picker_shown()
        self.select_comfort_option()
        text_order_button = self.actions.get_text(self.order_taxi_comfort)
        actions.assert_text_in_text(self.order_button_text, text_order_button)

# Verification code to set phone number
    def set_phone_verification_code(self):
        actions = self.actions
        code_verification = self.actions.retrieve_phone_code()
        actions.wait_visibility_of_element_located(self.phone_number_validation_sms_code_input_popup, 20)
        actions.set_input_text(self.phone_number_validation_sms_code_input_popup, code_verification)
        actions.assert_property_text(self.phone_number_validation_sms_code_input_popup, self.value, code_verification)
        actions.click(self.phone_number_validation_sms_confirm_button_popup)

# set phone number
    def set_phone_number(self):
        actions = self.actions
        phone_number = data.phone_number
        actions.scroll_element_into_view(self.phone_input)
        actions.click(self.phone_input)
        actions.wait_visibility_of_element_located(self.phone_number_title_popup, 10)
        actions.set_input_text(self.phone_number_input_popup, phone_number)
        actions.click(self.phone_number_submit_button_popup)
        self.set_phone_verification_code()
        actions.wait_visibility_of_element_located(self.phone_input, 10)
        actions.assert_input_text(self.phone_input, phone_number)

# Add card info
    def set_add_card_number(self):
        actions = self.actions
        card_number = data.card_number
        card_code = data.card_code
        actions.wait_visibility_of_element_located(self.add_card_number_popup, 20)
        actions.set_input_text(self.add_card_number_popup, card_number)
        actions.set_input_text(self.add_card_code_popup, card_code)
        actions.assert_property_text(self.add_card_number_popup, self.value, card_number)
        actions.assert_property_text(self.add_card_code_popup, self.value, card_code)
        actions.click(self.add_card_number_popup)
        actions.wait_visibility_of_element_located(self.add_card_submit_button_popup, 10)
        actions.click(self.add_card_submit_button_popup)

# Set a card payment as payment method
    def set_card_as_payment_method(self):
        actions = self.actions
        actions.scroll_element_into_view(self.pay_button)
        actions.assert_input_text(self.pay_method_selected, self.cash_text)
        actions.click(self.pay_button)
        actions.assert_is_selected(self.pay_method_cash_checkbox_popup)
        actions.click(self.pay_method_add_card_popup)
        self.set_add_card_number()
        actions.assert_is_selected(self.pay_method_card1_checkbox_popup)
        actions.click(self.pay_method_close_button_popup)
        actions.wait_visibility_of_element_located(self.pay_button, 10)
        actions.assert_input_text(self.pay_method_selected, self.card_text)

# Type a comment to the driver
    def set_comment(self):
        actions = self.actions
        actions.scroll_element_into_view(self.comment_input)
        comment = data.message_for_driver
        actions.set_input_text(self.comment_input, comment)
        actions.assert_property_text(self.comment_input, self.value, comment)

# Selected blancket and scarves
    def set_blanket_and_scarves(self):
        actions = self.actions
        actions.scroll_element_into_view(self.blanket_and_scarves_checkbox)
        actions.click(self.blanket_and_scarves_checkbox)
        actions.assert_is_selected(self.blanket_and_scarves_checkbox_selected)

# Selected two ice creams
    def set_ice_cream(self):
        actions = self.actions
        actions.scroll_element_into_view(self.ice_cream_counter)
        # assert no ice cream selected
        actions.assert_input_text(self.ice_cream_counter, str(0))
        actions.click(self.ice_cream_counter_plus)
        actions.click(self.ice_cream_counter_plus)
        # assert 2 ice cream selected
        actions.assert_input_text(self.ice_cream_counter, str(2))

# Modal of search taxi
    def modal_taxi_search(self):
        actions = self.actions
        new_text_order_button = actions.get_text(self.order_taxi_comfort)
        actions.assert_text_in_text(self.order_button_with_phone_number_text, new_text_order_button)
        actions.click(self.order_taxi_comfort)
        actions.wait_visibility_of_element_located(self.modal_searching_taxi_title, 10)
        actions.assert_is_displayed(self.modal_searching_taxi_title)
        actions.assert_input_text(self.modal_searching_taxi_title, self.modal_searching_taxi_title_text)
        actions.assert_is_displayed(self.modal_searching_taxi_time)
        actions.assert_is_displayed(self.modal_searching_taxi_cancel_button)
        actions.assert_is_displayed(self.modal_searching_taxi_details_button)
        actions.click(self.modal_searching_taxi_details_button)
        actions.assert_input_text(self.modal_searching_taxi_pickup_location, data.address_from)
        actions.assert_input_text(self.modal_searching_taxi_destination_address, data.address_to)
        actions.assert_input_text(self.modal_searching_taxi_payment_method, self.card_text)
        actions.assert_is_displayed(self.modal_searching_taxi_more_information)
