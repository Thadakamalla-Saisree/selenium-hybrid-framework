from uistore.international_bussiness_page_locators import International_Bussiness_Page_Locators
from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from utilities.excel_reader import ExcelReader


class International_Bussiness_Page:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Siva Komal
        Short description of method: Initializes the page object with required utilities
        Return type: None
        Parameter list: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.excel_reader = ExcelReader()
        self.helper = WebDriverHelper(self.driver)

    def click_on_international_business(self):
        """
        Method name: click_on_international_business
        Author name: Siva Komal
        Short description of method: Clicks on International Business option
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(International_Bussiness_Page_Locators.international_bussiness_nav_link)
            self.logger.info("Successfully clicked on International Business")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_international_business_failure")
            self.logger.error(f"Failed in click_on_international_business: {e}")
            raise

    def verify_url_is_present_of_international_business(self):
        """
        Method name: verify_url_is_present_of_international_business
        Author name: Siva Komal
        Short description of method: Verifies URL of International Business page
        Return type: None
        Parameter list: None
        """
        try:
            expected_url = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 2)
            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified the URL of International Business page")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_url_of_international_business_failure")
            self.logger.error(f"Failed in verify_url_of_international_business: {e}")
            raise

    def scroll_and_verify_text_is_present_certifications(self):
        """
        Method name: scroll_and_verify_text_is_present_certifications
        Author name: Siva Komal
        Short description of method: Scrolls to Certifications section and verifies text
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.scroll_till_particular_element(International_Bussiness_Page_Locators.certifications_section)
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.certifications_section, "Certifications")
            self.logger.info("Successfully verified Certifications text")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "scroll_and_verify_text_certifications_failure")
            self.logger.error(f"Failed in scroll_and_verify_text_certifications: {e}")
            raise

    def scroll_to_contact_and_message_forms(self):
        """
        Method name: scroll_to_contact_and_message_forms
        Author name: Siva Komal
        Short description of method: Scrolls to contact and message forms section
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.scroll_till_particular_element(International_Bussiness_Page_Locators.contact_and_message_section)
            self.logger.info("Successfully scrolled to contact and message forms")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "scroll_to_contact_and_message_forms_failure")
            self.logger.error(f"Failed in scroll_to_contact_and_message_forms: {e}")
            raise

    def verify_email_id_label(self):
        """
        Method name: verify_email_id_label
        Author name: Siva Komal
        Short description of method: Verifies Email ID label
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.email_id_label, "Email ID")
            self.logger.info("Successfully verified Email ID label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_email_id_label_failure")
            self.logger.error(f"Failed in verify_email_id_label: {e}")
            raise

    def enter_email_id(self):
        """
        Method name: enter_email_id
        Author name: Siva Komal
        Short description of method: Enters Email ID from excel
        Return type: None
        Parameter list: None
        """
        try:
            email = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 3)
            self.helper.send_data(International_Bussiness_Page_Locators.email_id_field, email)
            self.logger.info("Successfully entered Email ID")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_email_id_failure")
            self.logger.error(f"Failed in enter_email_id: {e}")
            raise

    def verify_phone_number_label(self):
        """
        Method name: verify_phone_number_label
        Author name: Siva Komal
        Short description of method: Verifies Phone Number label
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.phone_number_label, "Ph. No")
            self.logger.info("Successfully verified Phone Number label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_phone_number_label_failure")
            self.logger.error(f"Failed in verify_phone_number_label: {e}")
            raise

    def enter_phone_number(self):
        """
        Method name: enter_phone_number
        Author name: Siva Komal
        Short description of method: Enters phone number
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.send_data(International_Bussiness_Page_Locators.phone_number_field, "9876543210")
            self.logger.info("Successfully entered phone number")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_phone_number_failure")
            self.logger.error(f"Failed in enter_phone_number: {e}")
            raise

    def verify_country_label(self):
        """
        Method name: verify_country_label
        Author name: Siva Komal
        Short description of method: Verifies Country label
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.country_label, "Country")
            self.logger.info("Successfully verified Country label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_country_label_failure")
            self.logger.error(f"Failed in verify_country_label: {e}")
            raise

    def enter_country(self):
        """
        Method name: enter_country
        Author name: Siva Komal
        Short description of method: Enters country from excel
        Return type: None
        Parameter list: None
        """
        try:
            country = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 4)
            self.helper.send_data(International_Bussiness_Page_Locators.country_field, country)
            self.logger.info("Successfully entered country")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_country_failure")
            self.logger.error(f"Failed in enter_country: {e}")
            raise

    def verify_company_label(self):
        """
        Method name: verify_company_label
        Author name: Siva Komal
        Short description of method: Verifies Company Name label
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.company_label, "Company Name")
            self.logger.info("Successfully verified Company Name label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_company_label_failure")
            self.logger.error(f"Failed in verify_company_label: {e}")
            raise

    def enter_company_name(self):
        """
        Method name: enter_company_name
        Author name: Siva Komal
        Short description of method: Enters company name
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.send_data(International_Bussiness_Page_Locators.company_name_field, "Company")
            self.logger.info("Successfully entered company name")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_company_name_failure")
            self.logger.error(f"Failed in enter_company_name: {e}")
            raise

    def verify_address_label(self):
        """
        Method name: verify_address_label
        Author name: Siva Komal
        Short description of method: Verifies Address label
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.address_label, "Address")
            self.logger.info("Successfully verified Address label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_address_label_failure")
            self.logger.error(f"Failed in verify_address_label: {e}")
            raise

    def enter_address(self):
        """
        Method name: enter_address
        Author name: Siva Komal
        Short description of method: Enters address
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.send_data(International_Bussiness_Page_Locators.address_field, "Address")
            self.logger.info("Successfully entered address")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_address_failure")
            self.logger.error(f"Failed in enter_address: {e}")
            raise

    def verify_subject_label(self):
        """
        Method name: verify_subject_label
        Author name: Siva Komal
        Short description of method: Verifies Subject label
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.verify_text_is_present(International_Bussiness_Page_Locators.subject_label, "Subject")
            self.logger.info("Successfully verified Subject label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_subject_label_failure")
            self.logger.error(f"Failed in verify_subject_label: {e}")
            raise

    def enter_subject(self):
        """
        Method name: enter_subject
        Author name: Siva Komal
        Short description of method: Enters subject
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.send_data(International_Bussiness_Page_Locators.subject_field, "Subject")
            self.logger.info("Successfully entered subject")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_subject_failure")
            self.logger.error(f"Failed in enter_subject: {e}")
            raise

    def enter_message(self):
        """
        Method name: enter_message
        Author name: Siva Komal
        Short description of method: Enters message
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(International_Bussiness_Page_Locators.message_field)
            self.helper.send_data(International_Bussiness_Page_Locators.message_field, "message")
            self.logger.info("Successfully entered message")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "enter_message_failure")
            self.logger.error(f"Failed in enter_message: {e}")
            raise

    def click_on_send_button(self):
        """
        Method name: click_on_send_button
        Author name: Siva Komal
        Short description of method: Clicks on Send button and captures screenshot
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(International_Bussiness_Page_Locators.send_button)
            self.logger.info("Successfully clicked on Send button")
            Screenshot.capture_screenshot(self.driver, "Send button")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_send_button_failure")
            self.logger.error(f"Failed in click_on_send_button: {e}")
            raise

    def international_bussiness_page_flow(self):
        """
        Method name: international_bussiness_page_flow
        Author name: Siva Komal
        Short description of method: Executes the complete international bussiness page flow
        Return type: None
        Parameter list: None
        """
        try:
            self.click_on_international_business()
            self.verify_url_is_present_of_international_business()
            self.scroll_and_verify_text_is_present_certifications()
            self.scroll_to_contact_and_message_forms()
            self.verify_email_id_label()
            self.enter_email_id()
            self.verify_phone_number_label()
            self.enter_phone_number()
            self.verify_country_label()
            self.enter_country()
            self.verify_company_label()
            self.enter_company_name()
            self.verify_address_label()
            self.enter_address()
            self.verify_subject_label()
            self.enter_subject()
            self.enter_message()
            self.click_on_send_button()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "international bussiness page flow failure")
            self.logger.error(f"Failed in test_case_4_flow: {e}")
            raise
