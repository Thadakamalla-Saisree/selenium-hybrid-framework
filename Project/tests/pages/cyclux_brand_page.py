from uistore.cyclux_brand_page_locators import cyclux_brand_page_locators
from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from utilities.excel_reader import ExcelReader


class Cyclux_Brand_Page:
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

    def hover_on_cycles_by_brand(self):
        """
        Method name: hover_on_cycles_by_brand
        Author name: Siva Komal
        Short description of method: Hovers on Cycle's by brand menu
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.hover_on_one_element(cyclux_brand_page_locators.cycles_by_brand)
            self.logger.info("Successfully hovered on Cycle's by brand")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_on_cycles_by_brand_failure")
            self.logger.error(f"Failed in hover_on_cycles_by_brand: {e}")
            raise

    def click_on_cyclux(self):
        """
        Method name: click_on_cyclux
        Author name: Siva Komal
        Short description of method: Clicks on Cyclux brand from the dropdown
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.cyclux)
            self.logger.info("Successfully clicked on Cyclux")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_cyclux_failure")
            self.logger.error(f"Failed in click_on_cyclux: {e}")
            raise

    def verify_cyclux_label(self):
        """
        Method name: verify_cyclux_label
        Author name: Siva Komal
        Short description of method: Verifies Cyclux label text
        Return type: None
        Parameter list: None
        """
        try:
            cyclux_label = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 5)
            self.helper.verify_text_is_present(cyclux_brand_page_locators.cyclux_label,cyclux_label)
            self.logger.info("Successfully verified Cyclux label")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_cyclux_label_failure")
            self.logger.error(f"Failed in verify_cyclux_label: {e}")
            raise

    def click_on_sort(self):
        """
        Method name: click_on_sort
        Author name: Siva Komal
        Short description of method: Clicks on Sort dropdown
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.sort_dropdown)
            self.logger.info("Successfully clicked on Sort")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_sort_failure")
            self.logger.error(f"Failed in click_on_sort: {e}")
            raise

    def click_on_price_ascending(self):
        """
        Method name: click_on_price_ascending
        Author name: Siva Komal
        Short description of method: Selects price ascending option
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.price_ascending_option)
            self.logger.info("Successfully clicked on Price Ascending")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_price_ascending_failure")
            self.logger.error(f"Failed in click_on_price_ascending: {e}")
            raise

    def click_on_compare_icon(self):
        """
        Method name: click_on_compare_icon
        Author name: Siva Komal
        Short description of method: Clicks on compare icon for product
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.compare_icon)
            self.logger.info("Successfully clicked on compare icon")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_compare_icon_failure")
            self.logger.error(f"Failed in click_on_compare_icon: {e}")
            raise

    def click_on_cart_icon(self):
        """
        Method name: click_on_cart_icon
        Author name: Siva Komal
        Short description of method: Clicks on cart icon
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.cart_icon)
            self.logger.info("Successfully clicked on cart icon")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_cart_icon_failure")
            self.logger.error(f"Failed in click_on_cart_icon: {e}")
            raise

    def click_on_plus_symbol(self):
        """
        Method name: click_on_plus_symbol
        Author name: Siva Komal
        Short description of method: Clicks on plus symbol to increase quantity
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.plus_symbol)
            self.logger.info("Successfully clicked on plus symbol")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_plus_symbol_failure")
            self.logger.error(f"Failed in click_on_plus_symbol: {e}")
            raise

    def click_on_delete(self):
        """
        Method name: click_on_delete
        Author name: Siva Komal
        Short description of method: Clicks on delete button in cart
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.delete_btn)
            self.logger.info("Successfully clicked on delete")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_delete_failure")
            self.logger.error(f"Failed in click_on_delete: {e}")
            raise

    def cancel_alert(self):
        """
        Method name: cancel_alert
        Author name: Siva Komal
        Short description of method: Cancels/dismisses alert pop-up
        Return type: None
        Parameter list: None
        """
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            self.logger.info("Successfully dismissed the alert")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "cancel_alert_failure")
            self.logger.error(f"Failed in cancel_alert: {e}")
            raise

    def click_on_checkout(self):
        """
        Method name: click_on_checkout
        Author name: Siva Komal
        Short description of method: Clicks on checkout button
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(cyclux_brand_page_locators.checkout_btn)
            self.logger.info("Successfully clicked on checkout button")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_checkout_failure")
            self.logger.error(f"Failed in click_on_checkout: {e}")
            raise

    def verify_the_page_url(self):
        """
        Method name: verify_the_page_url
        Author name: Siva Komal
        Short description of method: Verifies the expected page URL using excel test data
        Return type: None
        Parameter list: None
        """
        try:
            expected_url = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 1)
            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified the url")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_page_url_failure")
            self.logger.error(f"Failed in verify_the_page_url: {e}")
            raise

    def verify_the_text_select_address(self):
        """
        Method name: verify_the_text_select_address
        Author name: Siva Komal
        Short description of method: Verifies checkout page section labels and captures screenshot
        Return type: None
        Parameter list: None
        """
        try:
            select_address_text = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 10)
            self.helper.verify_text_is_present(cyclux_brand_page_locators.select_address, select_address_text)
            price_details_text = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 7)
            self.helper.verify_text_is_present(cyclux_brand_page_locators.price_details,price_details_text)
            select_payment_method = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 8)
            self.helper.verify_text_is_present(cyclux_brand_page_locators.select_payment_method,select_payment_method)
            back_to_cart_data = self.excel_reader.get_data("cyclux_brand_page_sheet", 2, 9)
            self.helper.verify_text_is_present(cyclux_brand_page_locators.back_to_cart, back_to_cart_data)
            Screenshot.capture_screenshot(self.driver, "cyclux brand page")
            self.logger.info("Successfully verified all checkout labels and captured screenshot")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_text_select_address_failure")
            self.logger.error(f"Failed in verify_the_text_select_address: {e}")
            raise


    def cyclux_brand_page_flow(self):
        """
        Method name: cyclux_brand_page_flow
        Author name: Siva Komal
        Short description of method: Executes the complete cyclux brand page flow (clutter function)
        Return type: None
        Parameter list: None
        """
        try:
            self.hover_on_cycles_by_brand()
            self.click_on_cyclux()
            self.verify_cyclux_label()
            self.click_on_sort()
            self.click_on_price_ascending()
            self.click_on_compare_icon()
            self.click_on_cart_icon()
            self.click_on_plus_symbol()
            self.click_on_delete()
            self.cancel_alert()
            self.click_on_checkout()
            self.verify_the_page_url()
            self.verify_the_text_select_address()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "test_case_3_flow_failure")
            self.logger.error(f"Failed in cyclux brand page flow: {e}")
            raise

        





        

    
    


    







