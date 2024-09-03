import json
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import WebDriverException


class Actions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def set_input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_property_text(self, locator, attribute):
        return self.driver.find_element(*locator).get_property(attribute)

    def wait_visibility_of_element_located(self, locator, wait_time):
        WebDriverWait(self.driver, wait_time).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def scroll_element_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def element_is_selected(self, locator):
        return self.driver.find_element(*locator).is_selected()

    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def assert_is_selected(self, locator):
        assert self.element_is_selected(locator) == True

    def assert_is_displayed(self, locator):
        assert self.element_is_displayed(locator) == True

    def assert_input_text(self, locator, text):
        assert self.get_text(locator) == text

    def assert_property_text(self, locator, attribute, text):
        assert self.get_property_text(locator, attribute) == text

    @staticmethod
    def assert_text_in_text(in_text, text):
        assert in_text in text

    # no modificar
    def retrieve_phone_code(self) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

        driver = self.driver
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                  {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)  # este time.sleep() viene por defecto en esta funcion
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu "
                                "aplicación.")
            return code
