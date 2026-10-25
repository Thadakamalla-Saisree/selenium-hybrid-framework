from utilities.web_driver_helper import WebDriverHelper
from tests.uistore.checkout_page_locators import CheckoutPageLocators
from utilities.excel_reader import ExcelReader
from utilities.screenshot import Screenshot


class CheckOutHomePage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Prardhana
        Short description of method:
            Initializes the HomePage1 page object by assigning the WebDriver and logger,
            and creating required utility class instances (ExcelReader and WebDriverHelper)
            to support page actions and validations throughout the test flow.
        Return type: None
        Parameter list:
            driver (WebDriver): Selenium WebDriver instance used for browser actions
            logger (Logger): Logger instance used to record execution steps and failures
        """
        self.driver = driver
        self.logger = logger
        self.excel_reader = ExcelReader()
        self.helper = WebDriverHelper(self.driver)

    def click_search_and_enter_input_data(self):
        """
        Method name: click_search_and_enter_input_data
        Author name: Prardhana
        Short description of method:
            Navigates to the search area on the home page, focuses on the input field,
            reads the search keyword from the Excel test data sheet, enters the keyword
            into the search input, and triggers the search by clicking the search icon.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.search_bar)
            self.logger.info("Successfully clicked on search bar")

            self.helper.click_on_particular_element(CheckoutPageLocators.input_field)
            self.logger.debug("Successfully clicked on input field")

            search_term = self.excel_reader.get_data("check_out_sheet", 2, 1)
            self.logger.debug("Successfully fetched search term from excel")

            self.helper.send_data(CheckoutPageLocators.input_field, search_term)
            self.logger.info("Successfully entered gear in input field")

            self.helper.click_on_particular_element(CheckoutPageLocators.search_icon)
            self.logger.debug("Successfully clicked on search icon")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_search_and_enter_input_data_failure")
            self.logger.error(f"Failed in click_search_and_enter_input_data: {e}")

    def clicking_on_first_product_and_buynow(self):
        """
        Method name: clicking_on_first_product_and_buynow
        Author name: Prardhana
        Short description of method:
            Selects the first product displayed in the search results/product listing
            and proceeds further by clicking the 'Buy Now' option to initiate the
            checkout or purchase flow for the selected product.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.first_product)
            self.logger.info("Successfully clicked on first product")

            self.helper.click_on_particular_element(CheckoutPageLocators.buy_now)
            self.logger.debug("Successfully clicked buy now")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_on_first_product_and_buynow_failure")
            self.logger.error(f"Failed in clicking_on_first_product_and_buynow: {e}")

    def entering_name_and_email_input(self):
        """
        Method name: entering_name_and_email_input
        Author name: Prardhana
        Short description of method:
            Fills the customer details section by entering first name, last name, and email.
            The values are fetched from the Excel test data sheet and typed into the
            corresponding checkout form fields to continue the purchase process.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.first_name)
            fname = self.excel_reader.get_data("check_out_sheet", 2, 2)
            self.logger.debug("Successfully fetched first name from excel")

            self.helper.send_data(CheckoutPageLocators.first_name, fname)
            self.logger.info("Successfully entered name in first name field")

            self.helper.click_on_particular_element(CheckoutPageLocators.last_name)
            lname = self.excel_reader.get_data("check_out_sheet", 2, 3)
            self.logger.debug("Successfully fetched last name from excel")

            self.helper.send_data(CheckoutPageLocators.last_name, lname)
            self.logger.info("Successfully entered name in last name field")

            self.helper.click_on_particular_element(CheckoutPageLocators.email_input)
            email = self.excel_reader.get_data("check_out_sheet", 2, 4)
            self.logger.debug("Successfully fetched email from excel")

            self.helper.send_data(CheckoutPageLocators.email_input, email)
            self.logger.info("Successfully entered email in email field")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "entering_name_and_email_input_failure")
            self.logger.error(f"Failed in entering_name_and_email_input: {e}")

    def entering_number_and_pincode_input(self):
        """
        Method name: entering_number_and_pincode_input
        Author name: Prardhana
        Short description of method:
            Enters the contact number and pincode details on the checkout page by reading
            values from the Excel sheet. This step ensures the shipping/communication fields
            are populated as per the test data so the flow can proceed to the next stage.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.number_input)
            number = self.excel_reader.get_data("check_out_sheet", 2, 5)
            self.logger.debug("Successfully fetched number from excel")

            self.helper.send_data(CheckoutPageLocators.number_input, number)
            self.logger.info("Successfully entered number in number field")

            self.helper.click_on_particular_element(CheckoutPageLocators.pincode_input)
            pincode = self.excel_reader.get_data("check_out_sheet", 2, 6)
            self.logger.debug("Successfully fetched pincode from excel")

            self.helper.send_data(CheckoutPageLocators.pincode_input, pincode)
            self.logger.info("Successfully entered pincode in pincode field")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "entering_number_and_pincode_input_failure")
            self.logger.error(f"Failed in entering_number_and_pincode_input: {e}")

    def entering_adresses_input(self):
        """
        Method name: entering_adresses_input
        Author name: Prardhana
        Short description of method:
            Provides address-related details in the checkout form by filling state, city,
            and address fields. This method uses fixed placeholder strings for these fields
            to complete the address section and support end-to-end flow execution.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.state_input)
            state = self.excel_reader.get_data("check_out_sheet", 2, 7)
            self.logger.debug("Successfully fetched state from excel")

            self.helper.send_data(CheckoutPageLocators.state_input, state)
            self.logger.info("Successfully entered State in first State field")

            self.helper.click_on_particular_element(CheckoutPageLocators.city_input)
            city = self.excel_reader.get_data("check_out_sheet", 2, 8)
            self.logger.debug("Successfully fetched city from excel")

            self.helper.send_data(CheckoutPageLocators.city_input, city)
            self.logger.info("Successfully entered City in first City field")

            self.helper.click_on_particular_element(CheckoutPageLocators.address_input)
            address = self.excel_reader.get_data("check_out_sheet", 2, 9)
            self.logger.debug("Successfully fetched address from excel")

            self.helper.send_data(CheckoutPageLocators.address_input, address)
            self.logger.info("Successfully entered Address in first Address field")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "entering_adresses_input_failure")
            self.logger.error(f"Failed in entering_adresses_input: {e}")

    def entering_coupon_code(self):
        """
        Method name: entering_coupon_code
        Author name: Prardhana
        Short description of method:
            Enters a coupon code into the coupon input field and applies it by clicking
            the apply button. This step validates that the coupon section interaction
            can be performed successfully during the checkout process.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.coupn_code)
            code = self.excel_reader.get_data("check_out_sheet", 2, 10)
            self.logger.debug("Successfully fetched coupon code from excel")

            self.helper.send_data(CheckoutPageLocators.coupn_code, code)
            self.logger.info("Successfully entered Demo in coupon code field")

            self.helper.click_on_particular_element(CheckoutPageLocators.apply_button)
            self.logger.debug("Successfully clicked apply button")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "entering_coupon_code_failure")
            self.logger.error(f"Failed in entering_coupon_code: {e}")

    def clicking_razorpay_and_checkout(self):
        """
        Method name: clicking_razorpay_and_checkout
        Author name: Prardhana
        Short description of method:
            Selects the Razorpay payment option and proceeds by clicking the checkout button.
            This method ensures payment selection is performed before moving to the final
            confirmation stage of the order/payment workflow.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CheckoutPageLocators.razor_pay)
            self.logger.info("Successfully clicked razor pay")

            self.helper.click_on_particular_element(CheckoutPageLocators.check_out)
            self.logger.debug("Successfully clicked checkout")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_razorpay_and_checkout_failure")
            self.logger.error(f"Failed in clicking_razorpay_and_checkout: {e}")

    def verifying_text_and_screenshot(self):
        """
        Method name: verifying_text_and_screenshot
        Author name: Prardhana
        Short description of method:
            Verifies that the expected confirmation text 'PROCEED TO PAYMENT' is displayed
            on the final confirmation/control button. After successful verification, it
            captures an element screenshot and also captures an additional highlighted
            screenshot for visual evidence in reports.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(CheckoutPageLocators.verify_button, "PROCEED TO PAYMENT")
            self.logger.info("Successfully verified text proceed to payment")

            Screenshot.capture_element_screenshot(self.driver, CheckoutPageLocators.verify_button, "proceed.png")
            self.logger.debug("Successfully captured element screenshot proceed to payment")

            Screenshot.verify_text_is_present_and_capture_with_highlight(
                self.driver,
                CheckoutPageLocators.verify_button,
                "proceed.png",
                "abc"
            )
            self.logger.debug("Successfully captured highlighted screenshot proceed to payment")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verifying_text_and_screenshot_failure")
            self.logger.error(f"Failed in verifying_text_and_screenshot: {e}")

    def checkout_page_testcase(self):
        """
        Method name: checkout_page_testcase
        Author name: Prardhana
        Short description of method:
            Executes the complete end-to-end checkout workflow for test case 1 by calling
            each page-action method in sequence (search, product selection, user details,
            address details, coupon application, payment selection, and final verification).
            Any failure during execution is captured with screenshot and logged for analysis.
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.info("Starting checkout page testcase workflow")

            self.click_search_and_enter_input_data()
            self.clicking_on_first_product_and_buynow()

            self.logger.debug("Entering customer details (name, email, phone, pincode, address)")
            self.entering_name_and_email_input()
            self.entering_number_and_pincode_input()
            self.entering_adresses_input()

            self.logger.debug("Applying coupon and selecting payment method")
            self.entering_coupon_code()
            self.clicking_razorpay_and_checkout()

            self.verifying_text_and_screenshot()
            self.logger.info("Checkout page testcase workflow completed successfully")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "checkout_page_testcase_failure")
            self.logger.error(f"Failed in checkout_page_testcase: {e}")