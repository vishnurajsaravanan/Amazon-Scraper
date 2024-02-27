from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from amazoncaptcha import AmazonCaptcha

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

# assign your website to scrape
def captcha():
    driver.get('https://www.amazon.com/errors/validateCaptcha')

    link = driver.find_element(By.XPATH, '//div[@class="a-row a-text-center"]//img').get_attribute('src')

    captcha = AmazonCaptcha.fromlink(link)
    solution = AmazonCaptcha.solve(captcha)

    input_field = driver.find_element(By.ID, 'captchacharacters').send_keys(solution)

    button = driver.find_element(By.CLASS_NAME, 'a-button-text')
    button.click()
