from captcha import captcha
from keyword_search import keyword_search
from extract import *
from database import store_db

# get the captcha to enter into amazon site
captcha()
# enter the keyword to search for the item
keyword_search()

# scrape the amazon site    
scrape_amazon('wireless charger', 2)
