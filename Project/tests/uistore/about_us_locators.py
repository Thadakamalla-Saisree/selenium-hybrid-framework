from selenium.webdriver.common.by import By


class AboutUsLocators:
    about_us_link = about_us_link = (
        By.XPATH, "//a[@href='https://avoncycles.com/about/']")
    read_more_link = (By.XPATH, "//a[text()='Read more']")
    production_link = (By.XPATH, "//a[normalize-space()='Production']")
    career_link = (By.XPATH, "//a[@href='https://avoncycles.com/careers/']")
    apply_now_link = (By.XPATH, "//a[@data-fancybox and @href='#details']")
    life_at_avon_link = (By.XPATH, "//a[contains(@href,'/lifeatavon/')]")
    corporate_link = (By.XPATH, "//a[text()='Corporate']")
    annual_reports_image_link = (By.XPATH, "//div[@class='col-lg-4']")

    production_heading = (By.XPATH, "//h1[text()='Production']")
    # upload_your_job_profile = (
    #     By.XPATH, "//div[@id='details']/div/div[text()='Upload Your Job Profile']")

    upload_your_job_profile=(By.XPATH,"(//div[text()='Upload Your Job Profile'])[7]")
    
    close_icon_button = (
        By.XPATH, "//button[@class='fancybox-button fancybox-close-small']")