from captcha import *

def keyword_search():
# assign any keyword for searching
    keyword = "wireless charger"
    # create WebElement for a search box
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    # type the keyword in searchbox
    search_box.send_keys(keyword)
    # create WebElement for a search button
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    # click search_button
    search_button.click()
    # wait for the page to download
    driver.implicitly_wait(5)