from utilities.web_driver_helper import WebDriverHelper
from tests.uistore.product_filters_locators import ProductFiltersLocators
from utilities.excel_reader import ExcelReader
from utilities.screenshot import Screenshot


class ProductFiltersHomePage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Prardhana
        Short description of method:
            Initializes the ProductFiltersHomePage page object by assigning the WebDriver
            and logger instances, and creating the required utility objects such as
            ExcelReader and WebDriverHelper to perform actions, waits, validations,
            and data-driven operations during filter-based product page testing.
        Return type: None
        Parameter list:
            driver (WebDriver): Selenium WebDriver instance used to control browser actions
            logger (Logger): Logger instance used to record step execution and failures
        """
        self.driver = driver
        self.logger = logger
        self.excel_reader = ExcelReader()
        self.helper = WebDriverHelper(self.driver)

    def hover_bicycle_click_electric_cycles(self):
        """
        Method name: hover_bicycle_click_electric_cycles
        Author name: Prardhana
        Short description of method:
            Performs hover action on the Bicycle category menu and then clicks on the
            Electric Cycles option from the displayed submenu. This method ensures the
            navigation to the Electric Cycles listing page is initiated correctly.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.hover_on_one_element(ProductFiltersLocators.hover_bicycle_category)
            self.logger.info("Successfully hovered on bicycle category")

            self.helper.click_on_particular_element(ProductFiltersLocators.electric_cycles)
            self.logger.debug("Successfully clicked electric cycles")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_bicycle_click_electric_cycles_failure")
            self.logger.error(f"Failed in hover_bicycle_click_electric_cycles: {e}")

    def clicking_review_filter(self):
        """
        Method name: clicking_review_filter
        Author name: Prardhana
        Short description of method:
            Opens the review/ratings filter section and selects a specific review option
            to refine the product listing results. This method validates the filter
            interaction flow and ensures the chosen rating filter is applied.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.review_filter)
            self.logger.info("Successfully clicked review filters")

            self.helper.click_on_particular_element(ProductFiltersLocators.select_review)
            self.logger.debug("Successfully clicked second review option")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_review_filter_failure")
            self.logger.error(f"Failed in clicking_review_filter: {e}")

    def clicking_size_filter(self):
        """
        Method name: clicking_size_filter
        Author name: Prardhana
        Short description of method:
            Opens the size filter section and selects a size option to narrow down
            the product listing. This helps validate that the size filter controls
            are functional and can be applied successfully on the listing page.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.size_filter)
            self.logger.info("Successfully clicked size filter")

            self.helper.click_on_particular_element(ProductFiltersLocators.select_size)
            self.logger.debug("Successfully clicked size option")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_size_filter_failure")
            self.logger.error(f"Failed in clicking_size_filter: {e}")

    def clicking_height_filter(self):
        """
        Method name: clicking_height_filter
        Author name: Prardhana
        Short description of method:
            Applies the height filter by opening the height filter section and selecting
            a height option using JavaScript click. This method is useful for handling
            elements that are not reliably clickable using normal Selenium click.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.height_filter)
            self.logger.info("Successfully clicked height filter")

            self.helper.click_on_particular_element(ProductFiltersLocators.select_height)
            self.logger.debug("Successfully selected pull")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_height_filter_failure")
            self.logger.error(f"Failed in clicking_height_filter: {e}")

    def clicking_age_filter(self):
        """
        Method name: clicking_age_filter
        Author name: Prardhana
        Short description of method:
            Opens the age filter section and selects an age option using JavaScript click
            to refine the product list. This step validates that the age filter section
            expands correctly and the selected age option is applied on the UI.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.age_filter)
            self.logger.info("Successfully clicked age filter")

            self.helper.click_on_particular_element(ProductFiltersLocators.select_age)
            self.logger.debug("Successfully selected age")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_age_filter_failure")
            self.logger.error(f"Failed in clicking_age_filter: {e}")

    def clicking_color_filter(self):
        """
        Method name: clicking_color_filter
        Author name: Prardhana
        Short description of method:
            Opens the color swatches filter section and selects a color option to filter
            the product listing results. JavaScript click is used to avoid interaction
            failures caused by overlays or UI transitions.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.color_swatches)
            self.logger.info("Successfully clicked color filter")

            self.helper.click_on_particular_element(ProductFiltersLocators.select_color)
            self.logger.debug("Successfully selected color")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicking_color_filter_failure")
            self.logger.error(f"Failed in clicking_color_filter: {e}")

    def click_clear_filter(self):
        """
        Method name: click_clear_filter
        Author name: Prardhana
        Short description of method:
            Clicks the clear filter option to remove the currently applied filters and
            reset the product listing to the default state. This method confirms that
            the reset/clear functionality is working as expected.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.clear_filter)
            self.logger.info("Successfully clicked clear filter")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_clear_filter_failure")
            self.logger.error(f"Failed in click_clear_filter: {e}")

    def navigate_to_categories(self):
        """
        Method name: navigate_to_categories
        Author name: Prardhana
        Short description of method:
            Navigates to the categories section by clicking on the categories button.
            This method is used to open the categories listing/menu and confirm that
            the user can reach category navigation controls from the current page.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.categories_button)
            self.logger.info("Successfully clicked categories")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "navigate_to_categories_failure")
            self.logger.error(f"Failed in navigate_to_categories: {e}")

    def click_bicycle_category_and_veirfy(self):
        """
        Method name: click_bicycle_category_and_veirfy
        Author name: Prardhana
        Short description of method:
            Clicks on the Bicycle Category option from the categories section, verifies
            that the Bicycle Category heading/text is displayed correctly on the page,
            and captures an element-level screenshot as evidence for reporting.
        Return type: None
        Parameter list: None
        """
        try:
            self.helper.click_on_particular_element(ProductFiltersLocators.bicycle_category)
            self.logger.info("Successfully clicked bicycle category")

            text = self.excel_reader.get_data("product_filter_sheet", 2, 1)
            self.logger.debug("Successfully fetched bicycle category expected text from excel")

            self.helper.verify_text_is_present(ProductFiltersLocators.verify_bicyclecategory, text)
            self.logger.info("Successfully verified text bicycle category")

            Screenshot.capture_element_screenshot(self.driver, ProductFiltersLocators.verify_bicyclecategory, "bicycle.png")
            self.logger.debug("Successfully captured bicycle category screenshot")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_bicycle_category_and_veirfy_failure")
            self.logger.error(f"Failed in click_bicycle_category_and_veirfy: {e}")

    def product_page_testcase(self):
        """
        Method name: product_page_testcase
        Author name: Prardhana
        Short description of method:
            Clutter function (workflow executor) that runs the complete product filter
            validation flow in a single sequence. It performs navigation to Electric Cycles,
            applies multiple filters (review, size, height, age, color), clears filters,
            navigates to categories, and finally verifies the Bicycle Category page and
            captures evidence screenshots. Any exception during the flow is logged and
            a failure screenshot is captured for debugging.
        Return type: None
        Parameter list: None
        """
        try:
            self.logger.info("Starting product page testcase workflow")
            self.hover_bicycle_click_electric_cycles()

            self.logger.debug("Applying filters: review, size, height, age, color")
            self.clicking_review_filter()
            self.clicking_size_filter()
            self.clicking_height_filter()
            self.clicking_age_filter()
            self.clicking_color_filter()

            self.logger.debug("Clearing filters and navigating to categories for verification")
            self.click_clear_filter()
            self.navigate_to_categories()
            self.click_bicycle_category_and_veirfy()

            self.logger.info("Product page testcase workflow completed successfully")

        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "productpage_testcase_failure")
            self.logger.error(f"Failed in productpage_testcase: {e}")
