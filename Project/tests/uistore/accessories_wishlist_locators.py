from selenium.webdriver.common.by import By 

class Accessories_Wishlist_Locators:
    accessories_link = (By.XPATH, "//a[@class='nav-link']")
    first_product_heart_icon = (By.XPATH, "//span[@class='icon-heart']")
    
    login_email_input = (By.XPATH, "//input[@name='email']")
    login_password_input = (By.XPATH, "//input[@name='password']")
    
    login_button = (By.XPATH, "//button[@name='SubmitLogin']")
    verify_creds_mismatch_error = (By.XPATH, "//span[@class='help-block']")
    create_account_link = (By.XPATH, "(//a[contains(@href,'register')])[2]")

    first_name_input = (By.XPATH, "//input[@name='first_name']")
    last_name_input = (By.XPATH, "//input[@name='last_name']")
    register_email_input = (By.XPATH, "//input[@name='email']")
    register_phone_input = (By.XPATH, "//input[@name='phone']")
    register_password_input = (By.XPATH, "//input[@name='password']")
    register_password_confirm_input = (By.XPATH, "//input[@name='password_confirmation']")

    signup_btn = (By.ID, "sc_button-form-process")