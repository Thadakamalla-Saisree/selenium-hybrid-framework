from selenium.webdriver.common.by import By

class cyclux_brand_page_locators:
    cycles_by_brand = (By.XPATH,"//a[contains(text(),'by brand')]")
    cyclux = (By.XPATH,"//a[@href='https://avoncycles.com/brand/cyclux.html']")
    cyclux_label = (By.XPATH,"//h1")
    sort_dropdown = (By.XPATH,"//div[text()='Sort']")
    price_ascending_option = (By.ID,"bs-select-1-1")
    compare_icon = (By.XPATH,"//span[@class='icon-flip']")
    cart_icon = (By.XPATH,"//a[@class='btn']")
    plus_symbol= (By.CLASS_NAME,"cart-qty-plus")
    delete_btn = (By.CSS_SELECTOR,".icon-remove")
    checkout_btn = (By.ID,"checkout_btn")
    select_address = (By.XPATH,"//p[text()='Select Address']")
    price_details = (By.XPATH,"//h1[text()='Price Details']")
    select_payment_method = (By.XPATH,"//p[text()='Select Payment Method']")
    back_to_cart = (By.XPATH,"//button[text()='Back to cart']")
    