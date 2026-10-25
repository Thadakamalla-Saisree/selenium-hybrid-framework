import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.eventhandler import EventHandler
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

class WebDriverHelper:
    
    def __init__(self, driver):
        """
        Method name: __init__
        Author name: Saisree
        Short description of method:
            Initializes WebDriverHelper with WebDriver instance.
        Return type: None
        Parameter list:
            driver (WebDriver)
        """
        self.driver = driver

    
    def click_on_particular_element(self, locator):
        """
        Method name: click_on_particular_element
        Author name: Saisree
        Short description of method:
            Waits for an element to be visible and performs click action.
        Return type: None
        Parameter list:
            locator (tuple)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            element.click()

        except WebDriverException as e:
            print(e)
            raise Exception("Error in " + str(e))

    def send_data(self, locator, text):
        """
        Method name: send_data
        Author name: Saisree
        Short description of method:
            Sends text to the specified input element.
        Return type: None
        Parameter list:
            locator (tuple)
            text (str)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(text)

        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))

    def hover_on_one_element(self, locator):
        """
        Method name: hover_on_one_element
        Author name: Saisree
        Short description of method:
            Performs mouse hover action on an element.
        Return type: None
        Parameter list:
            locator (tuple)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            ActionChains(self.driver).move_to_element(element).perform()

        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))

    def scroll_till_particular_element(self, locator):
        """
        Method name: scroll_till_particular_element
        Author name: Saisree
        Short description of method:
            Scrolls the page until the specified element is visible.
        Return type: None
        Parameter list:
            locator (tuple)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", element
            )

        except Exception as e:
            print(f'An Error occured: {e}')

    def switch_to_new_window(self, index):
        """
        Method name: switch_to_new_window
        Author name: Saisree
        Short description of method:
            Switches browser control to a new window based on index.
        Return type: None
        Parameter list:
            index (int)
        """
        try:
            all_win = self.driver.window_handles
            new_win = all_win[index]
            self.driver.switch_to.window(new_win)

        except Exception as e:
            print(f'An Error ocured: {e}')

    def send_text_enter(self, locator, text):
        """
        Method name: send_text_enter
        Author name: Saisree
        Short description of method:
            Sends text to an element and presses ENTER key.
        Return type: None
        Parameter list:
            locator (tuple)
            text (str)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(text)
            element.send_keys(Keys.ENTER)

        except Exception as e:
            print(f'An Error ocured: {e}')
    
    def js_click_on_particular_element(self, locator):
        """
        Method name: js_click_on_particular_element
        Author name: Saisree
        Short description of method:
            Clicks on an element using JavaScript execution.
            This method is useful when normal click action fails.
        Return type: None
        Parameter list:
            locator (tuple)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )

            self.driver.execute_script(
                "arguments[0].click();", element
            )

        except Exception as e:
            print(f'An Error ocured: {e}')
    from selenium.webdriver.common.by import By


    def getElementsByXPATH(self, value):
        """
        Method name: getElementsByXPATH
        Author name: Saisree
        Short description of method:
            Finds and returns all web elements matching the given XPATH.

        Return type:
            list

        Parameter list:
            value (str): XPATH locator used to find elements
        """
        try:
            lst = self.driver.find_elements(By.XPATH, value)
            return lst
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in getElementsByXPATH: " + str(e))
    def select_an_element_in_dropdown(self, locator, text):
        """
        Method name: select_an_element_in_dropdown
        Author name: Saisree
        Short description of method:
            Selects the dropdown based on a particular value.
        Return type: None
        Parameter list:
            locator (tuple)
            text (str)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            select=Select(element)
            select.select_by_visible_text(text)


        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))
    


    def verify_text_is_present(self, locator, expected):
        """
        Method name: verify_text_is_present
        Author name: Saisree
        Short description of method:
            Verifies expected text is present in actual text.
        Return type: None
        Parameter list:
            actual (str)
            expected (str)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            actual=element.text
            assert expected in actual, (
                f"verify_text failed: Expected '{expected}' to be present in actual text '{actual}'."
            )
        except AssertionError:
            traceback.print_exc()
            raise
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in verify_text: " + str(e))


    def verify_title_is_present(self, expected):
        """
        Method name: verify_title_is_present
        Author name: Saisree
        Short description of method:
            Verifies expected text is present in the page title.
        Return type: None
        Parameter list:
            expected (str)
        """
        try:
            actual = self.driver.title
            assert expected in actual, (
                f"verify_title failed: Expected title to contain '{expected}', but got '{actual}'."
            )
        except AssertionError:
            traceback.print_exc()
            raise
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in verify_title: " + str(e))


    def verify_url_is_present(self, expected):
        """
        Method name: verify_url_is_present
        Author name: Saisree
        Short description of method:
            Verifies expected text is present in the current URL.
        Return type: None
        Parameter list:
            expected (str)
        """
        try:
            actual = self.driver.current_url
            assert expected in actual, (
                f"verify_url failed: Expected URL to contain '{expected}', but got '{actual}'."
            )
        except AssertionError:
            raise
        except WebDriverException as e:
            raise Exception("Error in verify_url: " + str(e))
                                

                