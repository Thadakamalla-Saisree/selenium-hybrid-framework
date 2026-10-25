from selenium.webdriver.common.by import By 

class CheckoutPageLocators:

    search_bar=(By.XPATH,"//span[contains(@class,'n-ic')]")
    input_field=(By.XPATH,"//input[@name='keyword']")
    search_icon=(By.XPATH,"//button[contains(@class,'it')]")

    first_product=(By.XPATH,"//div[contains(@class,'l-4')] //div[@class='top'] /descendant::a")

    buy_now=(By.ID,"productBuyNow")

    first_name=(By.XPATH,"//input[@name='first_name']") 
    last_name=(By.XPATH,"//input[@name='last_name']")
    email_input=(By.XPATH,"//input[@name='email']")
    number_input=(By.XPATH,"//input[@name='phone']")
    pincode_input=(By.XPATH,"//input[@name='postcode']")
    state_input=(By.XPATH,"//input[@name='address1']")
    city_input=(By.XPATH,"//input[@name='address2']")
    address_input=(By.XPATH,"//input[@name='address3']")

    coupn_code=(By.ID,"coupon-value")
    apply_button=(By.ID,"coupon-button") 
    razor_pay=(By.XPATH,"//div[@class='innerwrp']/descendant::span")

    check_out=(By.XPATH,"//div[@class='row']/descendant::button")
    
    verify_button=(By.CLASS_NAME,"confirm-btn")