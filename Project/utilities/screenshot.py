import os
import datetime
import time
from utilities.config_reader import ConfigReader


class Screenshot:

    @staticmethod
    def _get_screenshot_dir():
        """
        
        Author name: Prardhana
        
        """
        config = ConfigReader()
        path = config.get_value("PATH", "screenshot_path")
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    @staticmethod
    def _build_path(name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = Screenshot._get_screenshot_dir()
        filename = f"{name}_{timestamp}.png"
        return os.path.abspath(os.path.join(screenshot_dir, filename))

    # ✅ FULL PAGE screenshot (needed for your try/except blocks)
    @staticmethod
    def capture_screenshot(driver, name):
        """
        Author name: Prardhana
        Captures full page screenshot (viewport).
        """
        try:
            absolute_path = Screenshot._build_path(name)
            driver.save_screenshot(absolute_path)
            return absolute_path
        except Exception as error:
            raise Exception(f"Error while capturing screenshot: {error}")

    # ✅ ELEMENT-ONLY screenshot
    @staticmethod
    def capture_element_screenshot(driver, element_or_locator, name):
        """
        Captures ONLY the element screenshot (not full page)
        Author name: Prardhana
        Accepts:
            - WebElement
            - locator tuple like (By.CLASS_NAME, "confirm-btn") OR ("xpath","//...")
        """
        try:
            absolute_path = Screenshot._build_path(name)

            # If passed locator tuple, convert to WebElement
            element = element_or_locator
            if isinstance(element_or_locator, tuple):
                element = driver.find_element(*element_or_locator)

            # Scroll element to center for proper capture
            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", element
                )
                time.sleep(0.2)
            except Exception:
                pass

            element.screenshot(absolute_path)
            return absolute_path

        except Exception as error:
            raise Exception(f"Error while capturing element screenshot: {error}")

    # ✅ Verify text + neon highlight + element screenshot
    @staticmethod
    def verify_text_and_capture_with_highlight(
        driver,
        element_or_locator,
        expected_text,
        screenshot_name,
        contains=True,
        border_color="#39FF14",   # ✅ neon green by default
        border_thickness=3
    ):
        """
        Author name: Prardhana
        Verifies element text; if PASS, highlights border and captures element screenshot.
        """
        try:
            element = element_or_locator
            if isinstance(element_or_locator, tuple):
                element = driver.find_element(*element_or_locator)

            actual_text = (element.text or "").strip()
            expected_text = (expected_text or "").strip()

            is_verified = (expected_text in actual_text) if contains else (expected_text == actual_text)
            if not is_verified:
                return None

            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", element
                )
                time.sleep(0.2)
            except Exception:
                pass

            old_style = element.get_attribute("style") or ""

            try:
                highlight_style = (
                    f"{old_style}; "
                    f"border: {border_thickness}px solid {border_color}; "
                    f"box-shadow: 0 0 8px {border_color}, 0 0 16px {border_color}; "
                    f"box-sizing: border-box;"
                )

                driver.execute_script(
                    "arguments[0].setAttribute('style', arguments[1]);",
                    element,
                    highlight_style
                )
                time.sleep(0.2)

                return Screenshot.capture_element_screenshot(driver, element, screenshot_name)

            finally:
                try:
                    driver.execute_script(
                        "arguments[0].setAttribute('style', arguments[1]);",
                        element,
                        old_style
                    )
                except Exception:
                    pass

        except Exception as error:
            raise Exception(f"Error in verify_text_and_capture_with_highlight: {error}")