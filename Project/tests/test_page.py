import pytest
from base import BaseTest
from utilities.logger import configure_logger

from tests.pages.accessories_wishlist_page import Accessories_Wishlist_Authflow
from tests.pages.checkout_homepage import CheckOutHomePage
from tests.pages.product_filters_homepage import ProductFiltersHomePage
from tests.pages.cyclux_brand_page import Cyclux_Brand_Page
from tests.pages.international_bussiness_page import International_Bussiness_Page
from tests.pages.accolodes_and_awards_page import AccolodesandAwardsPage
from tests.pages.about_us_page import AboutUsPage
from tests.pages.avon_fitness_machine_page import AvonFitnessMachinePage
from tests.pages.home_page_footer_brand_actions import HomePageFooterBrandActions
from tests.pages.cambio_best_sellers_actions import CambioBestSellersActions


class Test_Page(BaseTest):
    logger = configure_logger()

    def setUp(self):
        url = "https://avoncycles.com/"
        self.driver = self.setUpDriver()
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.smoke
    def test_checkout_page(self):
        """
        Method name: test_checkout_page
        Author name: Prardhana
        Short description of method:
            Executes the complete functionality flow of the Checkout Page module
            using the page object and logs success or failure accordingly.
            In case of any exception, the error is logged and the exception
            is re-raised to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        try:
            checkout_page_obj = CheckOutHomePage(self.driver, self.logger)
            checkout_page_obj.checkout_page_testcase()
            self.logger.info("PASS: Checkout page complete functionality executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: Checkout page functionality execution failed.")
            self.logger.error(f"Exception: {e}")
            raise


    @pytest.mark.smoke
    def test_product_page(self):
        """
        Method name: test_product_page
        Author name: Prardhana
        Short description of method:
            Executes the complete functionality flow of the Product Page module
            using the page object and logs success or failure accordingly.
            In case of any exception, the error is logged and the exception
            is re-raised to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        try:
            product_page_obj = ProductFiltersHomePage(self.driver, self.logger)
            product_page_obj.product_page_testcase()
            self.logger.info("PASS: Product page complete functionality executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: Product page functionality execution failed.")
            self.logger.error(f"Exception: {e}")
            raise
    @pytest.mark.smoke
 

    def test_cycles_by_brand_cyclux(self):
        """
        Method name: test_cycles_by_brand_cyclux
        Author name: Siva Komal
        Short description of method:
            Executes the Cyclux brand page functionality flow
            and validates the complete process.
            Logs success or failure based on execution result.
        Return type: None
        Parameter list: None
        """
        try:
            Cyclux_brand_page_obj = Cyclux_Brand_Page(self.driver, self.logger)
            Cyclux_brand_page_obj.cyclux_brand_page_flow()
            self.logger.info("PASS: Cyclux brand page flow executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: Cyclux brand page flow execution failed.")
            self.logger.error(f"Exception: {e}")
            raise


    @pytest.mark.smoke
    def test_international_business(self):
        """
        Method name: test_international_business
        Author name: Siva Komal
        Short description of method:
            Executes the International Business page functionality
            and verifies successful execution of the flow.
            Logs success or failure accordingly.
        Return type: None
        Parameter list: None
        """
        try:
            international_business_obj = International_Bussiness_Page(self.driver, self.logger)
            international_business_obj.international_bussiness_page_flow()
            self.logger.info("PASS: International Business page flow executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: International Business page flow execution failed.")
            self.logger.error(f"Exception: {e}")
            raise


    @pytest.mark.smoke
    def test_accessories_wishlist(self):
        """
        Method name: test_accessories_wishlist
        Author name: Nishant Jadhav
        Short description of method:
            Execute click on  Accessories, add product to Wishlist.
            Filling Login & Signup forms.
            Use Verify text, verify url, verify title wherever required.
            Logs success or failure accordingly.
        Return type: None
        Parameter list: None
        """
        obj5 = Accessories_Wishlist_Authflow(self.driver, self.logger)
        obj5.test_case_5_flow()

    @pytest.mark.smoke
    def test_avon_fitness_machines(self):
        """
        Method name: test_avon_fitness_machines
        Author name: Saisree
        Short description of method:
            Executes the complete functionality flow of the Avon Fitness Machines module
            using the page object and logs success or failure accordingly. 
            In case of any exception, the error is logged with traceback and the exception 
            is re-raised to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        try:
            avon_fitness_machine_obj = AvonFitnessMachinePage(self.driver, self.logger)
            avon_fitness_machine_obj.avon_fitness_machine_complete_functionality()
            self.logger.info("PASS: Avon Fitness Machines complete functionality executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: Avon Fitness Machines functionality execution failed.")
            self.logger.error(f"Exception: {e}")
            
            raise
    

    @pytest.mark.smoke
    def test_accolodes_awards(self):
        """
        Method name: test_accolodes_awards
        Author name: Grace
        Short description of method:
            Executes the complete functionality flow of the Accolodes and Awards module
            using the corresponding page object and logs success or failure accordingly.
            In case of any exception, the error is logged and the exception
            is re-raised to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        try:
            accolodes_and_awards_object = AccolodesandAwardsPage(self.driver, self.logger)
            accolodes_and_awards_object.accolodes_and_awards_flow()
            self.logger.info("PASS: Accolodes and Awards page flow executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: Accolodes and Awards page flow execution failed.")
            self.logger.error(f"Exception: {e}")
            raise



    @pytest.mark.smoke
    def test_about_us_production_corporate(self):
        """
        Method name: test_about_us_production_corporate
        Author name: Grace
        Short description of method:
            Executes the complete About Us functionality flow including navigation
            through Production, Career, Apply Now, Life at Avon, Corporate, and
            Annual Reports using the page object and logs success or failure accordingly.
            In case of any exception, the error is logged and the exception
            is re-raised to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        try:
            about_us_object = AboutUsPage(self.driver, self.logger)
            about_us_object.about_us_flow()
            self.logger.info("PASS: About Us, Production, and Corporate flow executed successfully.")
        except Exception as e:
            self.logger.error("FAIL: About Us, Production, and Corporate flow execution failed.")
            self.logger.error(f"Exception: {e}")
            raise

    @pytest.mark.smoke
    def test_cycles_by_brand_color_swatches(self):
        """
        Method name: test_cycles_by_brand_color_swatches
        Author name: Anushka Deokar
        Short description of method:
            Executes the complete footer 'By Brand' flow on the Avon Cycles home page
            using the HomePageFooterBrandActions page object. The flow includes navigating
            to brand links from the footer, applying filter options (such as color swatches),
            sorting the product listing, opening a product, and validating key UI behavior
            such as visibility of Add to cart.
            In case of any exception, the error is logged and the exception is re-raised
            to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        home_page_footer_brand_obj = HomePageFooterBrandActions(self.driver, self.logger)
        home_page_footer_brand_obj.execute_footer_brand_filter_sort_flow()

    @pytest.mark.smoke
    def test_cycles_by_brand_cambio(self):
        """
        Method name: test_cycles_by_brand_cambio
        Author name: Anushka Deokar
        Short description of method:
            Executes the Cambio Best Sellers purchase flow using the CambioBestSellersActions
            page object. The flow includes navigating to the Cambio site, opening the Bikes menu,
            selecting the Best Sellers category, selecting a relevant option (e.g., 26T),
            adding a product to the cart, opening the cart, and proceeding towards checkout
            to validate the end-to-end shopping path.
            In case of any exception, the error is logged and the exception is re-raised
            to mark the test as failed.
        Return type: None
        Parameter list: None
        """
        cambio_best_sellers_actions_obj = CambioBestSellersActions(self.driver, self.logger)
        cambio_best_sellers_actions_obj.execute_cambio_best_sellers_purchase_flow()
