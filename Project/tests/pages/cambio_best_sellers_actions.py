from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from uistore.cambio_best_sellers_locators import CambioBestSellersLocators
from utilities.excel_reader import ExcelReader


class CambioBestSellersActions:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Anushka
        Short description of method:
            Initializes CambioBestSellersActions with WebDriver, logger, ExcelReader, and WebDriverHelper.
        Return type: None
        Parameter list: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.excel_reader = ExcelReader()
        self.helper = WebDriverHelper(self.driver)

    def open_cambio_site_link_and_switch_to_new_tab(self):
        """
        Method name: open_cambio_site_link_and_switch_to_new_tab
        Author name: Anushka
        Short description of method:
            Maximizes the browser window, scrolls to the Cambio site link, clicks it,
            and switches to the newly opened window/tab.
        Return type: None
        Parameter list: None
        """
        try:
            self.driver.maximize_window()
            self.helper.scroll_till_particular_element(CambioBestSellersLocators.cambio_site_link)
            self.helper.click_on_particular_element(CambioBestSellersLocators.cambio_site_link)
            self.logger.info("Successfully clicked on cambio")
            self.helper.switch_to_new_window(-1)
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_cambio_failure")
            self.logger.error(f"Failed to click on Cambio: {e}")
            raise

    def verify_cambio_page_url(self):
        """
        Method name: verify_cambio_page_url
        Author name: Anushka
        Short description of method:
            Reads expected Cambio URL from Excel and verifies the current URL.
        Return type: None
        Parameter list: None
        """
        try:
            expected_url = self.excel_reader.get_data("cambio_best_seller_actions", 2, 1)
            self.helper.verify_url_is_present(expected_url)
            self.logger.info("Successfully verified the url")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verifyUrl_failure")
            self.logger.error(f"Failed to verify the URL : {e}")
            raise

    def verify_cambio_page_title(self):
        """
        Method name: verify_cambio_page_title
        Author name: Anushka
        Short description of method:
            Verifies that the page title matches the expected 'Cambio' title from Excel.
        Return type: None
        Parameter list: None
        """
        try:
            cambio_title = self.excel_reader.get_data("cambio_best_seller_actions", 2, 6)
            self.helper.verify_title_is_present(cambio_title)
            self.logger.info("Successfully verified the title ")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verifyTitlecambio_failure")
            self.logger.error(f"Failed to verify the title cambio: {e}")
            raise

    def hover_on_bikes_menu_and_open_best_sellers_category(self):
        """
        Method name: hover_on_bikes_menu_and_open_best_sellers_category
        Author name: Anushka
        Short description of method:
            Hovers on the Bikes menu and clicks on the Best Sellers category option.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.hover_on_one_element(CambioBestSellersLocators.bikes_menu_item)
            self.helper.click_on_particular_element(CambioBestSellersLocators.best_sellers_category_link)
            self.logger.info("Successfully clicked on best_sellers")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "bikes_failure")
            self.logger.error(f"Failed to click on best sellers: {e}")
            raise

    def verify_best_sellers_page_title_and_scroll_to_product_categories(self):
        """
        Method name: verify_best_sellers_page_title_and_scroll_to_product_categories
        Author name: Anushka
        Short description of method:
            Verifies Best Sellers page title and scrolls to the Product categories section.
        Return type: None
        Parameter list: None
        """
        try:
            best_sellers = self.excel_reader.get_data("cambio_best_seller_actions", 2, 2)
            self.helper.verify_title_is_present(best_sellers)
            self.logger.info("Successfully verified the title")
            self.helper.scroll_till_particular_element(CambioBestSellersLocators.product_categories_section_title)
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verifyTitlebestsellers_failure")
            self.logger.error(f"Failed to verify the title Best Sellers: {e}")
            raise

    def verify_product_categories_section_title_is_displayed(self):
        """
        Method name: verify_product_categories_section_title_is_displayed
        Author name: Anushka
        Short description of method:
            Verifies that the 'Product categories' text is displayed on the page.
        Return type: None
        Parameter list: None
        """
        try:
            product_category = self.excel_reader.get_data("cambio_best_seller_actions", 2, 3)
            self.helper.verify_text_is_present(CambioBestSellersLocators.product_categories_section_title, product_category)
            self.logger.info("Successfully verified product category text")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_product_categories_failure")
            self.logger.error(f"Failed to verify the text product categories: {e}")
            raise

    def apply_26t_category_filter_and_open_select_options_on_first_product(self):
        """
        Method name: apply_26t_category_filter_and_open_select_options_on_first_product
        Author name: Anushka
        Short description of method:
            Clicks the 26T category filter, hovers on the first product in the list,
            and clicks on Select options for that product.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(CambioBestSellersLocators.category_26t_link)
            self.helper.hover_on_one_element(CambioBestSellersLocators.first_product_block)
            self.helper.click_on_particular_element(CambioBestSellersLocators.select_options_link)
            self.logger.info("Successfully selected the size")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_size_failure")
            self.logger.error(f"Failed to click the size of first product: {e}")
            raise

    def verify_26t_page_title_then_add_product_to_cart_and_open_cart(self):
        """
        Method name: verify_26t_page_title_then_add_product_to_cart_and_open_cart
        Author name: Anushka
        Short description of method:
            Verifies the page title is '26T', clicks Add to cart, then clicks View cart.
        Return type: None
        Parameter list: None
        """
        try:
            twenty_six = self.excel_reader.get_data("cambio_best_seller_actions", 2, 4)
            self.helper.verify_title_is_present(twenty_six)
            self.logger.debug("Successfully verified the title")

            self.helper.click_on_particular_element(CambioBestSellersLocators.add_to_cart_button)
            self.logger.debug("Successfully clicked on add to cart")

            self.helper.click_on_particular_element(CambioBestSellersLocators.view_cart_link)
            self.logger.info("Successfully clicked on view cart")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verifyTitle_failure")
            self.logger.error(f"Failed to Verify the title of 26T: {e}")
            raise

    def verify_cart_totals_and_proceed_to_checkout_with_screenshot(self):
        """
        Method name: verify_cart_totals_and_proceed_to_checkout_with_screenshot
        Author name: Anushka
        Short description of method:
            Verifies 'Cart totals' text, clicks Proceed to checkout,
            captures screenshot, and logs success message.
        Return type: None
        Parameter list: None
        """
        try:
            cart_totals = self.excel_reader.get_data("cambio_best_seller_actions", 2, 5)
            self.helper.verify_text_is_present(CambioBestSellersLocators.cart_totals_title, cart_totals)
            self.logger.debug("Successfully verified cart totals text ")

            self.helper.click_on_particular_element(CambioBestSellersLocators.proceed_to_checkout_link)
            self.logger.debug("Successfully clicked on proceed to checkout ")

            Screenshot.capture_screenshot(self.driver, "Proceed_to_Checkout")
            self.logger.info("Successfully clicked proceed to checkout button")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verifyCartTotals_failure")
            self.logger.error(f"Failed to Verify cart totals: {e}")
            raise

    def execute_cambio_best_sellers_purchase_flow(self):
        """
        Method name: execute_cambio_best_sellers_purchase_flow
        Author name: Anushka
        Short description of method:
            Executes the complete TC10 flow:
            open Cambio site → verify URL → verify title → open Best Sellers →
            verify Product categories → apply 26T filter → open Select options →
            verify 26T title → add to cart → view cart → verify cart totals → proceed to checkout.
        Return type: None
        Parameter list: None
        """
        try:
            self.open_cambio_site_link_and_switch_to_new_tab()
            self.verify_cambio_page_url()
            self.verify_cambio_page_title()
            self.hover_on_bikes_menu_and_open_best_sellers_category()
            self.verify_best_sellers_page_title_and_scroll_to_product_categories()
            self.verify_product_categories_section_title_is_displayed()
            self.apply_26t_category_filter_and_open_select_options_on_first_product()
            self.verify_26t_page_title_then_add_product_to_cart_and_open_cart()
            self.verify_cart_totals_and_proceed_to_checkout_with_screenshot()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "test_flow_ten_failure")
            self.logger.error(f"Failed test case 10: {e}")
            raise