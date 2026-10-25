from selenium.webdriver.common.by import By

class HomePageFooterBrandLocators:
    footer_by_brand_label = (By.XPATH, "//div[contains(text(),'By Brand')]")
    footer_by_brand_cyclux_link = (By.XPATH,"//ul[@class='links']/li/a[contains(@href,'cyclux')]")
    footer_by_brand_avon_link = (By.XPATH, "//a[text()='Avon']")

    filter_price_text = (By.XPATH, "//p[text()='Price']")
    filter_size_text = (By.XPATH, "//p[text()='Size']")
    size_filter_first_option_radio = (By.XPATH, "//input[@id='radio8']")

    filter_color_swatches_text = (By.XPATH, "//p[text()='Color Swatches']")
    clear_filter_button = (By.XPATH, "//button[text()='Clear Filter']")

    sort_dropdown = (By.XPATH, "//div[text()='Sort']")
    sort_price_ascending_option = (By.XPATH, "//span[text()='Price ascending']")

    first_product_image = (By.XPATH, "//div[@class='inner-image freeway-01 active']")
    add_to_cart_link = (By.XPATH, "//a[text()='Add to cart']")