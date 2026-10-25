from selenium.webdriver.common.by import By

class International_Bussiness_Page_Locators:
    international_bussiness_nav_link = (By.XPATH,"//a[@href='https://avoncycles.com/international-business']")
    avon_logo = (By.XPATH,"//img[@class='avon-int-logo']")
    certifications_section = (By.XPATH,"//div[text()='Certifications']")
    contact_and_message_section = (By.XPATH,"//div[text()='Contact & Message']")
    email_id_label = (By.XPATH,"//label[contains(text(),'Email ID')]")
    email_id_field = (By.ID,"name")
    phone_number_label = (By.XPATH,"//label[contains(text(),'Ph. No')]")
    phone_number_field = (By.XPATH,"//input[@name='phone']")
    country_label = (By.XPATH,"//label[text()='Country ']")
    country_field = (By.XPATH,"//input[@name='country']")
    company_label = (By.XPATH,"//label[text()='Company Name ']")
    company_name_field = (By.XPATH,"//input[@name='company_name']")
    address_label = (By.XPATH,"//label[text()='Address ']")
    address_field = (By.XPATH,"//input[@name='address']")
    subject_label = (By.XPATH,"//label[text()='Subject ']")
    subject_field = (By.XPATH,"//input[@name='subject']")
    message_field = (By.ID,"message")
    send_button = (By.XPATH,"//input[@class='btn btn-primary']")
    



