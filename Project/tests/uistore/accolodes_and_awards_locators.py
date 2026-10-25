from selenium.webdriver.common.by import By


class AccolodesandAwardsLocators:
    accolodes_and_awards_link = (By.XPATH, "//a[text()='Accolodes/Award']")
    blogs_link = (By.XPATH, "//a[text()='Blogs']")
    warranty_policy_link = (By.XPATH, "//a[text()='Warranty Policy']")
    terms_and_conditions_link = (
        By.XPATH, "//a[contains(@href,'/termcondition/')]")
    dealor_locator_link = (By.XPATH, "//a[contains(@href,'/storelocater')]")

    dealer_locator_heading = (
        By.XPATH, "//h1[@class='heading' and normalize-space()='Dealer Locator']")
    
    select_state_dropdown = (By.XPATH, "//select[@name='stateFilter']")

   