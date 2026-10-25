from utilities.web_driver_helper import WebDriverHelper
from uistore.about_us_locators import AboutUsLocators
from utilities.screenshot import Screenshot
from utilities.excel_reader import ExcelReader
from time import sleep


class AboutUsPage:
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

    def scroll_click_and_back(self, locator, element_name, screenshot_name,
                              wait_before_click=0, wait_after_click=0,
                              verify_locator=None, verify_text=None):
        """
        Method name: scroll_click_and_back
        Author name: Grace
        Short description of method:
            Reusable utility method to scroll to an element, click it,
            optionally verify text, and navigate back.
        Return type: None
        Parameter list:
            locator, element_name, screenshot_name,
            wait_before_click, wait_after_click,
            verify_locator, verify_text
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

            if verify_locator and verify_text:
                self.logger.debug(f"Verifying text '{verify_text}' is present for: {element_name}")
                self.helper.verify_text_is_present(verify_locator, verify_text)
                self.logger.info(f"Verified text '{verify_text}' successfully for {element_name}")

            self.logger.debug(f"Navigating back after clicking: {element_name}")
            self.driver.back()
            self.logger.info("Successfully gone back")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, f"{screenshot_name}_error")
            self.logger.error(f"Failed in scroll_click_and_back for {element_name}: {e}")
            raise

    def click_on_about_us(self):
        """
        Method name: click_on_about_us
        Author name: Grace
        Short description of method: Scrolls to About Us link, clicks it, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_and_back(
            locator=AboutUsLocators.about_us_link,
            element_name="About Us",
            screenshot_name="click_on_about_us"
        )

    def click_on_read_more(self):
        """
        Method name: click_on_read_more
        Author name: Grace
        Short description of method: Scrolls to Read More link, clicks it, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_and_back(
            locator=AboutUsLocators.read_more_link,
            element_name="Read More",
            screenshot_name="click_on_read_more"
        )

    def click_on_production(self):
        """
        Method name: click_on_production
        Author name: Grace
        Short description of method:
            Scrolls to Production link, clicks it, verifies heading, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_and_back(
            locator=AboutUsLocators.production_link,
            element_name="Production",
            screenshot_name="click_on_production",
            wait_before_click=2,
            wait_after_click=2,
            verify_locator=AboutUsLocators.production_heading,
            verify_text=self.excel_reader.get_data("about_us_and_awards", 2, 1)
        )

    def click_on_career(self):
        """
        Method name: click_on_career
        Author name: Grace
        Short description of method: Scrolls to Career link and clicks it
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Scrolling till Career link")
            self.helper.scroll_till_particular_element(AboutUsLocators.career_link)

            self.logger.debug("Clicking on Career link")
            self.helper.click_on_particular_element(AboutUsLocators.career_link)
            self.logger.info("Successfully clicked on Career")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_career_error")
            self.logger.error(f"Failed in click_on_career: {e}")
            raise

    def click_on_apply_now(self):
        """
        Method name: click_on_apply_now
        Author name: Grace
        Short description of method: Clicks Apply Now and verifies Upload Your Job Profile heading
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Clicking Apply Now link")
            self.helper.click_on_particular_element(AboutUsLocators.apply_now_link)

            self.logger.debug("Verifying 'Upload Your Job Profile' text")
            self.helper.verify_text_is_present(
                AboutUsLocators.upload_your_job_profile,
                self.excel_reader.get_data("about_us_and_awards", 2, 2)
            )
            self.logger.info("Successfully clicked on Apply Now and verified Upload Your Job Profile")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_apply_now_error")
            self.logger.error(f"Failed in click_on_apply_now: {e}")
            raise

    def click_on_close_icon(self):
        """
        Method name: click_on_close_icon
        Author name: Grace
        Short description of method: Clicks close icon and navigates back
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Clicking on Close Icon button")
            self.helper.click_on_particular_element(AboutUsLocators.close_icon_button)

            self.logger.debug("Navigating back after closing modal/page")
            self.driver.back()
            self.logger.info("Successfully clicked on Close Icon and navigated back")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_close_icon_error")
            self.logger.error(f"Failed in click_on_close_icon: {e}")
            raise

    def click_on_life_at_avon(self):
        """
        Method name: click_on_life_at_avon
        Author name: Grace
        Short description of method: Scrolls to Life at Avon link, clicks it, and navigates back
        Return type: None
        Parameter list: None
        """
        self.scroll_click_and_back(
            locator=AboutUsLocators.life_at_avon_link,
            element_name="Life at Avon",
            screenshot_name="click_on_life_at_avon"
        )

    def click_on_corporate(self):
        """
        Method name: click_on_corporate
        Author name: Grace
        Short description of method: Scrolls to Corporate link and clicks it
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Scrolling till Corporate link")
            self.helper.scroll_till_particular_element(AboutUsLocators.corporate_link)

            self.logger.debug("Clicking Corporate link")
            self.helper.click_on_particular_element(AboutUsLocators.corporate_link)
            self.logger.info("Successfully clicked on Corporate")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_corporate_error")
            self.logger.error(f"Failed in click_on_corporate: {e}")
            raise

    def click_on_annual_reports(self):
        """
        Method name: click_on_annual_reports
        Author name: Grace
        Short description of method: Clicks Annual Reports image, switches window, verifies URL, captures screenshot
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.debug("Clicking Annual Reports image link")
            self.helper.click_on_particular_element(AboutUsLocators.annual_reports_image_link)
            self.logger.info("Successfully clicked on Annual Reports")

            self.logger.debug("Switching to new window")
            self.helper.switch_to_new_window(-1)
            self.logger.info("Switched to new window successfully")

            self.logger.debug("Verifying URL contains: annual-reports")
            self.helper.verify_url_is_present("annual-reports")
            self.logger.info("Verified annual-reports URL successfully")

            Screenshot.capture_screenshot(self.driver, "testcase8")
            self.logger.info("Screenshot captured successfully: testcase8")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_annual_reports_error")
            self.logger.error(f"Failed in click_on_annual_reports: {e}")
            raise

    def about_us_flow(self):
        """
        Method name: about_us_flow
        Author name: Grace
        Short description of method:
            Executes the complete About Us navigation flow by performing sequential clicks
        Return type: None
        Parameter list: None
        """
        try:
            self.click_on_about_us()
            self.click_on_production()
            self.click_on_career()
            self.click_on_apply_now()
            self.click_on_close_icon()
            self.click_on_life_at_avon()
            sleep(2)
            self.click_on_corporate()
            sleep(2)
            self.click_on_annual_reports()
            sleep(2)
            self.logger.info("About Us flow completed successfully")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "about_us_flow_error")
            self.logger.error(f"About Us flow failed: {e}")
            raise