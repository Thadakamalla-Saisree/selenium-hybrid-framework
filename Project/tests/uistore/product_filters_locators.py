from selenium.webdriver.common.by import By 
class ProductFiltersLocators:
    hover_bicycle_category=(By.XPATH,"//li[contains(@class,'w')]")
    electric_cycles=(By.XPATH,"//a[contains(text(),'Bicycle Category')]/parent::li/div/a[contains(text(),'Electric Cycles')]") 
    click_price=(By.XPATH,"//img[@alt='Price-icon']")

    review_filter=(By.XPATH,"//img[@src='https://avoncycles.com/img/icon/listing/review.svg']")
    select_review=(By.ID,"radio5")

    size_filter=(By.XPATH,"//img[@src='https://avoncycles.com/img/icon/listing/frame-size.svg']")
    select_size=(By.ID,"radio8")

    height_filter=(By.XPATH,"//p[text()='Height (in feets)']")
    select_height=(By.ID,"radio9")

    age_filter=(By.XPATH,"//img[@src='https://avoncycles.com/img/icon/listing/age.svg']")
    select_age=(By.ID,"radio11")

    color_swatches=(By.XPATH,"//img[@src='https://avoncycles.com/img/icon/listing/colour.svg']")
    select_color=(By.ID,"radio12")

    clear_filter=(By.XPATH,"//div[contains(@class,'lter ')]/button")

    categories_button=(By.XPATH,"//a[@href='https://avoncycles.com/category']")

    bicycle_category=(By.XPATH,"//h5[contains(@class,'p')]")
    
    verify_bicyclecategory=(By.XPATH,"//h1[@class='heading mb-0']")
