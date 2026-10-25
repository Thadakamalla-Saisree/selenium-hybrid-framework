from selenium.webdriver.common.by import By
class AvonFitnessMachineLocator:
    avon_fitness_machine_button=(By.XPATH,"//a[text()='Avon Fitness Machines']")
    enquiry_form_close_button=(By.XPATH,"//button[@class='close']")
    domestic_gym_suggestion=(By.XPATH,"//a[text()='Domestic Gym ']")
    cardio_line_suggestion=(By.XPATH,"//a[text()='Domestic Gym ']/parent::li/descendant::span[text()='Cardio Line']")
    trademills_suggestion=(By.XPATH,"(//a[text()='Treadmills '])[2]")
    trademills_first_product=(By.XPATH,"//a[text()='Enquire Now ']")
    specifications_text=(By.XPATH,"//h3[@class='normal fullWidth text-center mb-3']")
    enquiry_now_button=(By.XPATH,"//span[text()='Enquire Now']")
    enquiry_form_product_name_text=(By.XPATH,"//label[text()='Product Name']")
    enquiry_form_product_model_text=(By.XPATH,"//label[text()='Product Model']")
    enquiry_form_name_field=(By.ID,"product_enquiry_name")
    enquiry_form_email_field=(By.ID,"product_enquiry_email")
    enquiry_form_phone_field=(By.ID,"product_enquiry_phone")
    enquiry_form_city_field=(By.ID,"product_enquiry_city")
    enquiry_form_submit_btn=(By.XPATH,"//button[@class='btn btn-primary sub-btn']")
    

