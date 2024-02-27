from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from captcha import * 
from database import store_db

keyword = 'wireless charger'
next_page = ''

def scrape_amazon(keyword, max_pages):
    page_number = 1

    driver.implicitly_wait(5)
    keyword = keyword
    search = driver.find_element(By.XPATH,'//*[(@id = "twotabsearchtextbox")]')
    search.send_keys(keyword)
    # click search button
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()

    driver.implicitly_wait(5)
    
    while page_number <= max_pages:
        scrape_page(driver)
        # driver.get(next_page)
        driver.implicitly_wait(5)
        page_number += 1
    driver.quit()

    

def scrape_page(driver):
    product_asin = []
    product_name = []
    product_price = []
    product_ratings = []
    product_ratings_num = []
    product_link = []

    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for item in items:
        # find name
        name = item.find_element(By.XPATH,'.//span[@class="a-size-medium a-color-base a-text-normal"]')
        product_name.append(name.text)

        # find ASIN number 
        data_asin = item.get_attribute("data-asin")
        product_asin.append(data_asin)

        # find price
        whole_price = item.find_elements(By.XPATH,'.//span[@class="a-price-whole"]')
        fraction_price = item.find_elements(By.XPATH,'.//span[@class="a-price-fraction"]')
        
        if whole_price != [] and fraction_price != []:
            price = '.'.join([whole_price[0].text, fraction_price[0].text])
        else:
            price = 0
        product_price.append(price)

        # find ratings box
        ratings_box = item.find_elements(By.XPATH,'.//div[@class="a-row a-size-small"]/span')

        # find ratings and ratings_num
        if ratings_box != []:
            ratings = ratings_box[0].get_attribute('aria-label')
            ratings_num = ratings_box[1].get_attribute('aria-label')
        else:
            ratings, ratings_num = 0,0
        
        product_ratings.append(str(ratings))
        product_ratings_num.append(str(ratings_num))

        # find link
        link = item.find_element(By.XPATH,'.//a[@class="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute("href")
        product_link.append(link)

    global next_page
    next_page_element = driver.find_element(By.XPATH, '//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    store_db(product_asin, product_name, product_price, product_ratings, product_ratings_num, product_link)

    return next_page