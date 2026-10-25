from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from uistore.avon_fitness_machines_locator import AvonFitnessMachineLocator
from utilities.excel_reader import ExcelReader


class AvonFitnessMachinePage:
    """
    Class name: AvonFitnessMachinePage
    Author name: Saisree
    Short description:
        Page Object class that handles footer navigation to Avon Fitness Machines site,
        performs category navigation, opens product, verifies specification section,
        and submits enquire form using Excel test data.
    """

    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saisree
        Short description of method:
            Initializes AvonFitnessMachinePage with WebDriver, logger, WebDriverHelper, and ExcelReader.
        Return type: None
        Parameter list: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(self.driver)
        self.excel_reader = ExcelReader()

    

    def scroll_to_footer_and_click_on_avon_fitness_machines(self):
        """
        Method name: scroll_to_footer_and_click_on_avon_fitness_machines
        Author name: Saisree
        Short description of method:
            Scrolls to footer, clicks on Avon Fitness Machines link,
            and switches to the newly opened window.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.scroll_till_particular_element(AvonFitnessMachineLocator.avon_fitness_machine_button)
            self.logger.info("Successfully scrolled to the footer section")

            self.helper.click_on_particular_element(AvonFitnessMachineLocator.avon_fitness_machine_button)
            self.logger.info("Successfully clicked on Avon Fitness Machines link")

            self.helper.switch_to_new_window(-1)
            self.logger.info("Successfully switched to the new window")
        except Exception as e:
            Screenshot.capture_screenshot(
                self.driver, "scroll_footer_click_avon_fitness_machines_failure"
            )
            self.logger.error(f"Failed in footer navigation or window switch: {e}")
            raise

    def verify_the_page(self):
        """
        Method name: verify_the_page
        Author name: Saisree
        Short description of method:
            Verifies that the redirected URL belongs to Avon Fitness Machines website.
        Return type: None
        Parameter list: None
        """
        try:
            url=self.excel_reader.get_data("avon_fitness_machine", 2, 1)
            self.helper.verify_url_is_present(url)
            self.logger.info("Successfully verified Avon Fitness Machines URL")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_page_failure")
            self.logger.error(f"Failed to verify the url for the avon fitness machine: {e}")
            raise

    def hover_on_domestic_gym(self):
        """
        Method name: hover_on_domestic_gym
        Author name: Saisree
        Short description of method:
            Closes the popup form if present and hovers on Domestic Gym menu.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_form_close_button)
            self.logger.debug("Popup form close button clicked (if present)")

            self.helper.hover_on_one_element(AvonFitnessMachineLocator.domestic_gym_suggestion)
            self.logger.info("Successfully hovered on Domestic Gym menu")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_on_domestic_gym_failure")
            self.logger.error(f"Failed to hover on Domestic Gym menu: {e}")
            raise

    def hover_on_cardio_line(self):
        """
        Method name: hover_on_cardio_line
        Author name: Saisree
        Short description of method:
            Hovers on Cardio Line submenu.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.hover_on_one_element(AvonFitnessMachineLocator.cardio_line_suggestion)
            self.logger.info("Successfully hovered on Cardio Line menu")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_on_cardio_line_failure")
            self.logger.error(f"Failed to hover on Cardio Line menu: {e}")
            raise

    def click_on_treadmills(self):
        """
        Method name: click_on_treadmills
        Author name: Saisree
        Short description of method:
            Clicks on Treadmills option under Domestic Gym > Cardio Line.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.trademills_suggestion)
            self.logger.info("Successfully clicked on Treadmills category")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_treadmills_failure")
            self.logger.error(f"Failed to click on Treadmills category: {e}")
            raise

    def verify_the_url(self):
        """
        Method name: verify_the_url
        Author name: Saisree
        Short description of method:
            Verifies that user is navigated to the Domestic Treadmills page URL.
        Return type: None
        Parameter list: None
        """
        try:
            url=self.excel_reader.get_data("avon_fitness_machine", 2, 2)
            self.helper.verify_url_is_present(url)
            self.logger.info("Successfully verified Domestic Treadmills page URL")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_url_failure")
            self.logger.error(f"Failed to verify Domestic Treadmills URL: {e}")
            raise

    def click_on_first_product(self):
        """
        Method name: click_on_first_product
        Author name: Saisree
        Short description of method:
            Clicks on the first product displayed in Domestic Treadmills listing.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.trademills_first_product)
            self.logger.info("Successfully clicked on the first treadmill product")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_first_product_failure")
            self.logger.error(f"Failed to click on the first product: {e}")
            raise

    def verify_specifications(self):
        """
        Method name: verify_specifications
        Author name: Saisree
        Short description of method:
            Verifies the presence of SPECIFICATIONS section text on product page.
        Return type: None
        Parameter list: None
        """
        try:
            text=self.excel_reader.get_data("avon_fitness_machine", 2,3 )
            
            self.helper.verify_text_is_present(AvonFitnessMachineLocator.specifications_text, text)
            self.logger.info("Successfully verified SPECIFICATIONS text on product page")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_specifications_failure")
            self.logger.error(f"Failed to verify SPECIFICATIONS section: {e}")
            raise

    def click_on_enquire_now(self):
        """
        Method name: click_on_enquire_now
        Author name: Saisree
        Short description of method:
            Clicks on the Enquire Now button/link for the selected product.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_now_button)
            self.logger.info("Successfully clicked on Enquire Now")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_enquire_now_failure")
            self.logger.error(f"Failed to click Enquire Now: {e}")
            raise

    def verify_product_name_and_product_model(self):
        """
        Method name: verify_product_name_and_product_model
        Author name: Saisree
        Short description of method:
            Verifies the Product Name and Product Model fields are available on enquiry form.
        Return type: None
        Parameter list: None
        """
        try:
            prod_name=self.excel_reader.get_data("avon_fitness_machine", 2, 4)
            
            self.helper.verify_text_is_present(AvonFitnessMachineLocator.enquiry_form_product_name_text, prod_name)
            self.logger.info("Successfully verified Product Name field presence")
            prod_model=self.excel_reader.get_data("avon_fitness_machine", 2, 5)
            

            self.helper.verify_text_is_present(AvonFitnessMachineLocator.enquiry_form_product_model_text, prod_model)
            self.logger.info("Successfully verified Product Model field presence")
        except Exception as e:
            Screenshot.capture_screenshot(
                self.driver, "verify_product_name_and_product_model_failure"
            )
            self.logger.error(f"Failed to verify Product Name/Model fields: {e}")
            raise

    def enter_the_name(self):
        """
        Method name: enter_the_name
        Author name: Saisree
        Short description of method:
            Reads name from Excel and enters it into the Name field.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_form_name_field)

            name = self.excel_reader.get_data("avon_fitness_machine", 2, 6)
            self.logger.debug(f"Name fetched from Excel: {name}")

            self.helper.send_data(AvonFitnessMachineLocator.enquiry_form_name_field, name)
            self.logger.info("Successfully entered the Name in enquiry form")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_the_name_failure")
            self.logger.error(f"Failed to enter Name in enquiry form: {e}")
            raise

    def enter_the_email(self):
        """
        Method name: enter_the_email
        Author name: Saisree
        Short description of method:
            Reads email from Excel and enters it into the Email field.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_form_email_field)

            email = self.excel_reader.get_data("avon_fitness_machine", 2, 7)
            self.logger.debug(f"Email fetched from Excel: {email}")

            self.helper.send_data(AvonFitnessMachineLocator.enquiry_form_email_field, email)
            self.logger.info("Successfully entered the Email in enquiry form")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_the_email_failure")
            self.logger.error(f"Failed to enter Email in enquiry form: {e}")
            raise

    def enter_the_phone(self):
        """
        Method name: enter_the_phone
        Author name: Saisree
        Short description of method:
            Reads phone from Excel and enters it into the Phone field.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_form_phone_field)

            phone = self.excel_reader.get_data("avon_fitness_machine", 2, 8)
            self.logger.debug(f"Phone fetched from Excel: {phone}")

            self.helper.send_data(AvonFitnessMachineLocator.enquiry_form_phone_field, phone)
            self.logger.info("Successfully entered the Phone number in enquiry form")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_the_phone_failure")
            self.logger.error(f"Failed to enter Phone number in enquiry form: {e}")
            raise

    def enter_the_city(self):
        """
        Method name: enter_the_city
        Author name: Saisree
        Short description of method:
            Reads city from Excel and enters it into the City field.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_form_city_field)

            city = self.excel_reader.get_data("avon_fitness_machine", 2, 9)
            self.logger.debug(f"City fetched from Excel: {city}")

            self.helper.send_data(AvonFitnessMachineLocator.enquiry_form_city_field, city)
            self.logger.info("Successfully entered the City in enquiry form")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_the_city_failure")
            self.logger.error(f"Failed to enter City in enquiry form: {e}")
            raise

    def click_on_submit(self):
        """
        Method name: click_on_submit
        Author name: Saisree
        Short description of method:
            Clicks the Submit button and captures a screenshot after submission.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(AvonFitnessMachineLocator.enquiry_form_submit_btn)
            self.logger.info("Successfully clicked on Submit button")

            Screenshot.capture_screenshot(self.driver, "captured_screenshot")
            self.logger.info("Successfully captured screenshot after form submission")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_submit_failure")
            self.logger.error(f"Failed to submit enquiry form: {e}")
            raise

    def avon_fitness_machine_complete_functionality(self):
        """
        Method name: avon_fitness_machine_complete_functionality
        Author name: Saisree
        Short description of method:
            Executes complete end-to-end Avon Fitness Machine flow:
            navigation from Avon Cycles footer to Avon Fitness Machines,
            category selection, product verification, enquiry form submission.
        Return type: None
        Parameter list: None
        """
        try:
            
            self.scroll_to_footer_and_click_on_avon_fitness_machines()
            self.verify_the_page()
            self.hover_on_domestic_gym()
            self.hover_on_cardio_line()
            self.click_on_treadmills()
            self.verify_the_url()
            self.click_on_first_product()
            self.verify_specifications()
            self.click_on_enquire_now()
            self.verify_product_name_and_product_model()
            self.enter_the_name()
            self.enter_the_email()
            self.enter_the_phone()
            self.enter_the_city()
            self.click_on_submit()

            self.logger.info("Completed Testcase 6 end-to-end flow successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "avon_fitness_machine_complete_functionality")
            self.logger.error(f"Avon fitness machine complete end-to-end flow failed: {e}")
            raise