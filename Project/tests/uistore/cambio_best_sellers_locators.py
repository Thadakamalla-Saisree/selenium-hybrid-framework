from selenium.webdriver.common.by import By


class CambioBestSellersLocators:
    cambio_site_link = (By.XPATH, "//a[text()='Cambio']")
    bikes_menu_item = (By.XPATH, "//li[@id='menu-item-5201']")
    best_sellers_category_link = (By.XPATH, "//a[@href='https://cambiobikes.com/product-category/best-sellers/']")

    product_categories_section_title = (By.XPATH, "//span[text()='Product categories']")
    category_26t_link = (By.XPATH, "//a[text()='26T']")

    first_product_block = (By.XPATH, "//div[@class='product-block']")
    select_options_link = (By.XPATH, "//a[text()='Select options']")

    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    view_cart_link = (By.XPATH, "//a[text()='View cart']")

    cart_totals_title = (By.XPATH, "//h2[text()='Cart totals']")
    proceed_to_checkout_link = (By.XPATH, "//a[@href='https://cambiobikes.com/checkout/']")
