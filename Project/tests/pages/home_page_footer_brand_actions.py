from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from uistore.home_page_footer_brand_locators import HomePageFooterBrandLocators
from utilities.excel_reader import ExcelReader


class HomePageFooterBrandActions:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Anushka
        Short description of method:
            Initializes HomePageFooterBrandActions with WebDriver, logger, ExcelReader, and WebDriverHelper.
        Return type: None
        Parameter list: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.excel_reader = ExcelReader()
        self.helper = WebDriverHelper(self.driver)

    def scroll_to_footer_by_brand_section(self):
        """
        Method name: scroll_to_footer_by_brand_section
        Author name: Anushka
        Short description of method:
            Maximizes the browser window and scrolls down to the footer 'By Brand' section
            where the Cyclux link is present.
        Return type: None
        Parameter list: None
        """
        try:
            self.driver.maximize_window()
            self.helper.scroll_till_particular_element(HomePageFooterBrandLocators.footer_by_brand_cyclux_link)
            self.logger.info("scroll down")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "scroll_footer_failure")
            self.logger.error(f" Failed  to scroll till footer : {e}")
            raise

    def verify_footer_by_brand_section_title(self):
        """
        Method name: verify_footer_by_brand_section_title
        Author name: Anushka
        Short description of method:
            Verifies that the "Cycle's By Brand" label/title is displayed in the footer By Brand section.
        Return type: None
        Parameter list: None
        """
        try:
            expected_label = self.excel_reader.get_data("home_page_footer_brand", 2, 3)
            self.helper.verify_text_is_present(HomePageFooterBrandLocators.footer_by_brand_label, expected_label)
            self.logger.info("Successfully verified label for cycle's brand")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_label_failure")
            self.logger.error(f"Failed to  verify label : {e}")
            raise

    def open_cyclux_brand_link_from_footer(self):
        """
        Method name: open_cyclux_brand_link_from_footer
        Author name: Anushka
        Short description of method:
            Clicks on the Cyclux brand link under the footer By Brand section.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(HomePageFooterBrandLocators.footer_by_brand_cyclux_link)
            self.logger.info("Successfully clicked on cyclux")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_cyclux_failure")
            self.logger.error(f"Failed click_cyclux : {e}")
            raise

    def verify_cyclux_brand_url_and_navigate_back(self):
        """
        Method name: verify_cyclux_brand_url_and_navigate_back
        Author name: Anushka
        Short description of method:
            Reads expected Cyclux URL from Excel, verifies current URL,
            then navigates back to the previous page to continue execution.
        Return type: None
        Parameter list: None
        """
        try:
            expected_url = self.excel_reader.get_data("home_page_footer_brand", 2, 1)
            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified the url")
            self.driver.back()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_url_one_failure")
            self.logger.error(f"Failed to  verify  url of cyclux: {e}")
            raise

    def open_avon_brand_link_from_footer(self):
        """
        Method name: open_avon_brand_link_from_footer
        Author name: Anushka
        Short description of method:
            Scrolls to the Avon brand link under footer By Brand section and clicks it.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.scroll_till_particular_element(HomePageFooterBrandLocators.footer_by_brand_avon_link)
            self.helper.click_on_particular_element(HomePageFooterBrandLocators.footer_by_brand_avon_link)
            self.logger.info("Successfully clicked on Avon")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_avon_failure")
            self.logger.error(f"Failed to  click avon : {e}")
            raise

    def verify_avon_brand_url(self):
        """
        Method name: verify_avon_brand_url
        Author name: Anushka
        Short description of method:
            Reads expected Avon URL from Excel and verifies the current URL after navigation.
        Return type: None
        Parameter list: None
        """
        try:
            expected_url = self.excel_reader.get_data("home_page_footer_brand", 2, 2)
            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified the URL")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_url_two_failure")
            self.logger.error(f"Failed to Verify the URL of Avon page : {e}")
            raise

    def verify_price_filter_label_is_displayed(self):
        """
        Method name: verify_price_filter_label_is_displayed
        Author name: Anushka
        Short description of method:
            Verifies that the 'Price' label/text is displayed on the page for the Price filter section.
        Return type: None
        Parameter list: None
        """
        try:
            price = self.excel_reader.get_data("home_page_footer_brand", 2, 5)
            self.helper.verify_text_is_present(HomePageFooterBrandLocators.filter_price_text, price)
            self.logger.info("Successfully verified the text")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_Text_failure")
            self.logger.error(f"Failed to verify the text : {e}")
            raise

    def apply_size_filter_select_first_option_and_clear_filters(self):
        """
        Method name: apply_size_filter_select_first_option_and_clear_filters
        Author name: Anushka
        Short description of method:
            Opens Size filter, selects the first available size option,
            opens Color Swatches filter, and clears all applied filters.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(HomePageFooterBrandLocators.filter_size_text)
            self.logger.debug("Successfully clicked on size filter")

            self.helper.click_on_particular_element(HomePageFooterBrandLocators.size_filter_first_option_radio)
            self.logger.debug("Successfully clicked on first option")

            self.helper.click_on_particular_element(HomePageFooterBrandLocators.filter_color_swatches_text)
            self.logger.debug("Successfully clicked on color swatch")

            self.helper.click_on_particular_element(HomePageFooterBrandLocators.clear_filter_button)
            self.logger.info("Successfully clicked on clear filter")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "select_size_failure")
            self.logger.error(f"Failed to select the size of cycle: {e}")
            raise

    def sort_products_by_price_ascending(self):
        """
        Method name: sort_products_by_price_ascending
        Author name: Anushka
        Short description of method:
            Opens Sort dropdown and selects 'Price ascending' to sort the product listing.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(HomePageFooterBrandLocators.sort_dropdown)
            self.helper.click_on_particular_element(HomePageFooterBrandLocators.sort_price_ascending_option)
            self.logger.info("Successfully selected ascending dropdown")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "drop_failure")
            self.logger.error(f"Failed to select price from dropdown: {e}")
            raise

    def open_first_product_from_listing(self):
        """
        Method name: open_first_product_from_listing
        Author name: Anushka
        Short description of method:
            Clicks on the first product displayed in the listing after applying filter/sorting.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(HomePageFooterBrandLocators.first_product_image)
            self.logger.info("Successfully clicked on first product")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "first_prod_failure")
            self.logger.error(f"Failed to Click on first product: {e}")
            raise

    def verify_add_to_cart_button_text_and_capture_screenshot(self):
        """
        Method name: verify_add_to_cart_button_text_and_capture_screenshot
        Author name: Anushka
        Short description of method:
            Verifies that the Add to cart button text is displayed and captures a screenshot for evidence.
        Return type: None
        Parameter list: None
        """
        try:
            add_cart = self.excel_reader.get_data("home_page_footer_brand", 2, 4)
            self.helper.verify_text_is_present(HomePageFooterBrandLocators.add_to_cart_link, add_cart)
            self.logger.info("Successfully verified add to cart")
            Screenshot.capture_screenshot(self.driver, "Clicked_on_first_product")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_add_cart_button_failure")
            self.logger.error(f"Failed to verify_add_cart_button: {e}")
            raise

    def execute_footer_brand_filter_sort_flow(self):
        """
        Method name: execute_footer_brand_filter_sort_flow
        Author name: Anushka
        Short description of method:
            Executes the complete TC9 flow:
            scroll to footer By Brand → open Cyclux → verify URL → back → open Avon → verify URL →
            verify Price label → apply Size and Color Swatches filters → clear filters →
            sort by Price ascending → open first product → verify Add to cart.
        Return type: None
        Parameter list: None
        """
        try:
            self.scroll_to_footer_by_brand_section()
            self.verify_footer_by_brand_section_title()
            self.open_cyclux_brand_link_from_footer()
            self.verify_cyclux_brand_url_and_navigate_back()
            self.open_avon_brand_link_from_footer()
            self.verify_avon_brand_url()
            self.verify_price_filter_label_is_displayed()
            self.apply_size_filter_select_first_option_and_clear_filters()
            self.sort_products_by_price_ascending()
            self.open_first_product_from_listing()
            self.verify_add_to_cart_button_text_and_capture_screenshot()
            self.verify_add_to_cart_button_text_and_capture_screenshot()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "test_flow_nine_failure")
            self.logger.error(f"Failed test case 9: {e}")
            raise
        