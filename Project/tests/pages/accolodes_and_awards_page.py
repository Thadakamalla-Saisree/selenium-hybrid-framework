from utilities.web_driver_helper import WebDriverHelper
from uistore.accolodes_and_awards_locators import AccolodesandAwardsLocators
from utilities.screenshot import Screenshot
from utilities.excel_reader import ExcelReader
from time import sleep

class AccolodesandAwardsPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Grace
        Short description of method: Initializes the page object with required utilities
        Return type: None
        Parameter list: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(self.driver)
        self.excel_reader = ExcelReader()

    def scroll_click_verify_and_back(self, locator, element_name, screenshot_name,
                                    expected_url=None, wait_before_click=0, wait_after_click=0):
        """
        Method name: scroll_click_verify_and_back
        Author name: Grace
        Short description of method:
            Reusable method to scroll till element, click it, optionally verify URL,
            and navigate back. Includes debug + info logs.
        Return type: None
        Parameter list:
            locator, element_name, screenshot_name, expected_url,
            wait_before_click, wait_after_click
        """
        try:
            self.logger.debug(f"Scrolling till element: {element_name} | locator: {locator}")
            self.helper.scroll_till_particular_element(locator)

            if wait_before_click:
                self.logger.debug(f"Waiting {wait_before_click}s before clicking: {element_name}")
                sleep(wait_before_click)

            self.logger.debug(f"Clicking on element: {element_name}")
            self.helper.click_on_particular_element(locator)
            self.logger.info(f"Successfully clicked on {element_name}")

            if wait_after_click:
                self.logger.debug(f"Waiting {wait_after_click}s after clicking: {element_name}")
                sleep(wait_after_click)

            if expected_url:
                self.logger.debug(f"Verifying URL is present: {expected_url} | for: {element_name}")
                self.helper.verify_url_is_present(expected_url)
                self.logger.info(f"Verified URL successfully for {element_name}")

            self.logger.debug(f"Navigating back after clicking: {element_name}")
            self.driver.back()
            self.logger.info("Navigated back successfully")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, f"{screenshot_name}_error")
            self.logger.error(f"Failed in scroll_click_verify_and_back for {element_name}: {e}")
            raise

    def click_on_accolodes_and_award(self):
        """
        Method name: click_on_accolodes_and_award
        Author name: Grace
        Short description of method: Scrolls to footer, clicks Accolodes/Award, verifies URL, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_verify_and_back(
            locator=AccolodesandAwardsLocators.accolodes_and_awards_link,
            element_name="Accolodes and Awards",
            screenshot_name="click_on_accolodes_and_award",
            expected_url=self.excel_reader.get_data("about_us_and_awards", 2, 4)
        )

    def click_on_blogs(self):
        """
        Method name: click_on_blogs
        Author name: Grace
        Short description of method: Scrolls to footer, clicks Blogs, verifies URL, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_verify_and_back(
            locator=AccolodesandAwardsLocators.blogs_link,
            element_name="Blogs",
            screenshot_name="click_on_blogs",
            expected_url=self.excel_reader.get_data("about_us_and_awards", 2, 5)
        )

    def click_on_warranty_policy(self):
        """
        Method name: click_on_warranty_policy
        Author name: Grace
        Short description of method: Scrolls to footer, clicks Warranty Policy, verifies URL, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_verify_and_back(
            locator=AccolodesandAwardsLocators.warranty_policy_link,
            element_name="Warranty Policy",
            screenshot_name="click_on_warranty_policy",
            expected_url=self.excel_reader.get_data("about_us_and_awards", 2, 6)
        )

    def click_on_terms_and_conditions(self):
        """
        Method name: click_on_terms_and_conditions
        Author name: Grace
        Short description of method: Scrolls to footer, clicks Terms & Conditions, verifies URL, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_verify_and_back(
            locator=AccolodesandAwardsLocators.terms_and_conditions_link,
            element_name="Terms and Conditions",
            screenshot_name="click_on_terms_and_conditions",
            expected_url=self.excel_reader.get_data("about_us_and_awards", 2, 7)
        )

    def click_on_dealor_locator(self):
        """
        Method name: click_on_dealor_locator
        Author name: Grace
        Short description of method:
            Clicks Dealer Locator link, verifies URL, and verifies heading text
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Clicking on Dealer Locator link")
            self.helper.click_on_particular_element(AccolodesandAwardsLocators.dealor_locator_link)
            self.logger.info("Successfully clicked on Dealor Locator")

            self.logger.debug("Verifying Dealer Locator page URL")
            
            self.helper.verify_url_is_present(self.excel_reader.get_data("about_us_and_awards", 2, 8))
            self.logger.info("Verified Dealer Locator page URL successfully")

            self.logger.debug("Verifying Dealer Locator heading text")
            self.helper.verify_text_is_present(
                AccolodesandAwardsLocators.dealer_locator_heading,
                self.excel_reader.get_data("about_us_and_awards", 2, 3)
            )
            self.logger.info("Verified Dealer Locator heading successfully")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_dealor_locator_error")
            self.logger.error(f"Failed in click_on_dealor_locator: {e}")
            raise

    def select_state_as_assam(self):
        """
        Method name: select_state_as_assam
        Author name: Grace
        Short description of method: Selects Assam from State dropdown
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Selecting State dropdown value: Assam")
            self.helper.select_an_element_in_dropdown(
                AccolodesandAwardsLocators.select_state_dropdown,
                self.excel_reader.get_data("about_us_and_awards", 2, 9)
            )
            self.logger.info("Successfully selected State as Assam")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "select_state_as_assam_error")
            self.logger.error(f"Failed in select_state_as_assam: {e}")
            raise

    
    def accolodes_and_awards_flow(self):
        """
        Method name: accolodes_and_awards_flow
        Author name: Grace
        Short description of method:
            Executes the complete Useful Links and Dealer Locator flow
        Return type: None
        Parameter list: None
        """
        try:
            self.click_on_accolodes_and_award()
            self.click_on_blogs()
            self.click_on_warranty_policy()
            self.click_on_terms_and_conditions()
            self.click_on_dealor_locator()
            self.select_state_as_assam()
            

            self.logger.info("Accolodes and Awards flow completed successfully")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "accolodes_and_awards_flow_error")
            self.logger.error(f"Accolodes and Awards flow failed: {e}")
            raise