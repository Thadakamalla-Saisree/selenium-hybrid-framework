from datetime import datetime
from time import sleep

from utilities.web_driver_helper import WebDriverHelper
from tests.uistore.accessories_wishlist_locators import Accessories_Wishlist_Locators
from utilities.excel_reader import ExcelReader
from utilities.screenshot import Screenshot


class Accessories_Wishlist_Authflow:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Nishant Jitendra Jadhav
        Short description of method: Initializes the Accessories_Wishlist_Authflow object with required utilities
        Return type: None
        Parameter list: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.excel_reader = ExcelReader()
        self.helper = WebDriverHelper(self.driver)

        self.logger.info("Accessories_Wishlist_Authflow initialized successfully")
        self.logger.debug(f"Driver: {self.driver}, Helper: {self.helper}, ExcelReader: {self.excel_reader}")

    # ----------------------------- Utility Methods -----------------------------

    def _timestamp(self):
        """Returns timestamp string for unique screenshot names."""
        self.logger.info("Generating timestamp")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.logger.debug(f"Generated timestamp: {ts}")
        return ts

    def _failure_handler(self, method_name: str, error: Exception):
        """
        Method name: _failure_handler
        Author name: Nishant Jitendra Jadhav
        Short description of method: Captures screenshot + logs failure message in a standard format
        Return type: None
        Parameter list: method_name, error
        """
        self.logger.info(f"Failure handler triggered for: {method_name}")
        self.logger.debug(f"Error object received: {repr(error)}")

        screenshot_name = f"Accessories_Wishlist_Authflow_{method_name}_failure_{self._timestamp()}"
        self.logger.debug(f"Capturing failure screenshot with name: {screenshot_name}")

        Screenshot.capture_screenshot(self.driver, screenshot_name)
        self.logger.error(f"Failed in {method_name}: {error}", exc_info=True)

    def _evidence_screenshot(self, step_name: str):
        """
        Method name: _evidence_screenshot
        Author name: Nishant Jitendra Jadhav
        Short description of method: Captures evidence screenshot with proper naming
        Return type: None
        Parameter list: step_name
        """
        self.logger.info(f"Capturing evidence screenshot for step: {step_name}")
        self.logger.debug(f"Step name received for screenshot: {step_name}")

        screenshot_name = f"Accessories_Wishlist_Authflow_{step_name}_success_{self._timestamp()}"
        self.logger.debug(f"Evidence screenshot name: {screenshot_name}")

        Screenshot.capture_screenshot(self.driver, screenshot_name)

    # ----------------------------- Page Actions -----------------------------

    def click_on_accessories(self):
        """
        Method name: click_on_accessories
        Author name: Nishant Jitendra Jadhav
        Short description of method: Clicks Accessories link and verifies redirected URL
        Return type: None
        Parameter list: None
        """
        self.logger.info("Starting click_on_accessories")
        self.logger.debug(f"Using locator: {Accessories_Wishlist_Locators.accessories_link}")

        try:
            self.helper.click_on_particular_element(Accessories_Wishlist_Locators.accessories_link)
            self.logger.info("Successfully clicked on Accessories link")
            self.logger.debug("Click action completed on Accessories link")

            expected_url = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 1)
            self.logger.debug(f"Expected Accessories URL (Excel): {expected_url}")

            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified Accessories page URL")
            self.logger.debug("Accessories URL verification completed")

            self._evidence_screenshot("accessories_page")

        except Exception as e:
            self._failure_handler("click_on_accessories", e)

    def click_on_heart_icon(self):
        """
        Method name: click_on_heart_icon
        Author name: Nishant Jitendra Jadhav
        Short description of method: Clicks heart icon for first product and switches to new window
        Return type: None
        Parameter list: None
        """
        self.logger.info("Starting click_on_heart_icon")
        self.logger.debug(f"Using locator: {Accessories_Wishlist_Locators.first_product_heart_icon}")

        try:
            self.helper.click_on_particular_element(Accessories_Wishlist_Locators.first_product_heart_icon)
            self.logger.info("Successfully clicked on first product heart icon")
            self.logger.debug("Heart icon click executed")

            self.helper.switch_to_new_window(-1)
            self.logger.info("Successfully switched to new window/tab")
            self.logger.debug("Switched to last opened window/tab using index -1")

            self._evidence_screenshot("after_heart_click")

        except Exception as e:
            self._failure_handler("click_on_heart_icon", e)

    def fill_login_form(self):
        """
        Method name: fill_login_form
        Author name: Nishant Jitendra Jadhav
        Short description of method: Verifies login page URL/title, fills login details and validates error text
        Return type: None
        Parameter list: None
        """
        self.logger.info("Starting fill_login_form")
        self.logger.debug("Reading Login URL/Title and credentials from Excel")

        try:
            expected_url = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 2)
            self.logger.debug(f"Expected Login URL (Excel): {expected_url}")
            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified Login page URL")
            self.logger.debug("Login URL verification completed")

            page_title = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 4)
            self.logger.debug(f"Expected Login Title (Excel): {page_title}")
            self.helper.verify_title_is_present(page_title)
            self.logger.info("Successfully verified Login page title")
            self.logger.debug("Login title verification completed")

            email_value = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 5)
            password_value = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 6)
            self.logger.debug(f"Fetched login data -> email: {email_value}, password_length: {len(str(password_value))}")

            self.helper.send_data(Accessories_Wishlist_Locators.login_email_input, email_value)
            self.logger.info("Successfully entered email in login email field")
            self.logger.debug(f"Email entered in locator: {Accessories_Wishlist_Locators.login_email_input}")

            self.helper.send_data(Accessories_Wishlist_Locators.login_password_input, password_value)
            self.logger.info("Successfully entered password in login password field")
            self.logger.debug(f"Password entered in locator: {Accessories_Wishlist_Locators.login_password_input}")

            self.helper.click_on_particular_element(Accessories_Wishlist_Locators.login_button)
            self.logger.info("Successfully clicked on Login button")
            self.logger.debug(f"Clicked locator: {Accessories_Wishlist_Locators.login_button}")

            sleep(2)
            self.logger.debug("Static wait applied: 2 seconds")

            creds_error = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 7)
            self.logger.debug(f"Expected creds mismatch error (Excel): {creds_error}")

            self.helper.verify_text_is_present(Accessories_Wishlist_Locators.verify_creds_mismatch_error, creds_error)
            self.logger.info("Successfully verified credentials mismatch error message")
            self.logger.debug("Mismatch error text verification completed")

            self._evidence_screenshot("login_error_verified")

            self.helper.click_on_particular_element(Accessories_Wishlist_Locators.create_account_link)
            self.logger.info("Successfully clicked on Create Account link")
            self.logger.debug(f"Clicked locator: {Accessories_Wishlist_Locators.create_account_link}")

        except Exception as e:
            self._failure_handler("fill_login_form", e)

    def fill_register_form(self):
        """
        Method name: fill_register_form
        Author name: Nishant Jitendra Jadhav
        Short description of method: Verifies register page URL and fills registration form fields
        Return type: None
        Parameter list: None
        """
        self.logger.info("Starting fill_register_form")
        self.logger.debug("Reading Register URL and registration form data from Excel")

        try:
            register_url = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 3)
            self.logger.debug(f"Expected Register URL (Excel): {register_url}")
            self.helper.verify_url_is_present(register_url)
            self.logger.info("Successfully verified Register page URL")
            self.logger.debug("Register URL verification completed")

            first_name = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 8)
            last_name = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 9)
            email = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 5)
            phone = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 10)
            password = self.excel_reader.get_data("accessories_wishlist_sheet", 2, 11)

            self.logger.debug(
                f"Fetched register data -> first_name: {first_name}, last_name: {last_name}, "
                f"email: {email}, phone: {phone}, password_length: {len(str(password))}"
            )

            self.helper.send_data(Accessories_Wishlist_Locators.first_name_input, first_name)
            self.logger.info("Successfully entered first name in register form")
            self.logger.debug(f"Entered first name locator: {Accessories_Wishlist_Locators.first_name_input}")

            self.helper.send_data(Accessories_Wishlist_Locators.last_name_input, last_name)
            self.logger.info("Successfully entered last name in register form")
            self.logger.debug(f"Entered last name locator: {Accessories_Wishlist_Locators.last_name_input}")

            self.helper.send_data(Accessories_Wishlist_Locators.register_email_input, email)
            self.logger.info("Successfully entered email in register form")
            self.logger.debug(f"Entered email locator: {Accessories_Wishlist_Locators.register_email_input}")

            self.helper.send_data(Accessories_Wishlist_Locators.register_phone_input, phone)
            self.logger.info("Successfully entered phone number in register form")
            self.logger.debug(f"Entered phone locator: {Accessories_Wishlist_Locators.register_phone_input}")

            self.helper.send_data(Accessories_Wishlist_Locators.register_password_input, password)
            self.logger.info("Successfully entered password in register form")
            self.logger.debug(f"Entered password locator: {Accessories_Wishlist_Locators.register_password_input}")

            self.helper.send_data(Accessories_Wishlist_Locators.register_password_confirm_input, password)
            self.logger.info("Successfully entered confirm password in register form")
            self.logger.debug(f"Entered confirm password locator: {Accessories_Wishlist_Locators.register_password_confirm_input}")

            self.helper.click_on_particular_element(Accessories_Wishlist_Locators.signup_btn)
            self.logger.info("Successfully clicked on sign up button")
            self.logger.debug(f"Clicked signup button locator: {Accessories_Wishlist_Locators.signup_btn}")

            self._evidence_screenshot("register_form_filled")

        except Exception as e:
            self._failure_handler("fill_register_form", e)

    def test_case_5_flow(self):
        """
        Method name: test_case_5_flow
        Author name: Nishant Jitendra Jadhav
        Short description of method: Executes end-to-end flow for testcase 5
        Return type: None
        Parameter list: None
        """
        self.logger.info("Successfully started test_case_5_flow")
        self.logger.debug("Flow steps: Accessories -> Heart icon -> Login -> Register")

        try:
            self.click_on_accessories()
            self.logger.debug("Completed step: click_on_accessories")

            self.click_on_heart_icon()
            self.logger.debug("Completed step: click_on_heart_icon")

            self.fill_login_form()
            self.logger.debug("Completed step: fill_login_form")

            self.fill_register_form()
            self.logger.debug("Completed step: fill_register_form")

            self.logger.info("Successfully completed test_case_5_flow")
            self.logger.debug("test_case_5_flow executed successfully")

        except Exception as e:
            self._failure_handler("test_case_5_flow", e)