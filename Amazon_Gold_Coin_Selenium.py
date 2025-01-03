""" 
Developer Name: MARUTHACHALAM S
Project Title: Gold Coin Search in Amazon Website using Python Selenium
Date: 03.01.2025
Version 1

 """ 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import re

def data_clean(data):
    data = re.sub('&amp;','&',str(data))
    data = re.sub('&quot;',"'",str(data))
    data = re.sub('&nbsp;','',str(data))
    data = re.sub('&#39;;',"';",str(data))
    data = re.sub('&#39;',"';",str(data))
    data = re.sub('&#xD;&#xA;',' ',str(data))
    data = re.sub('#x27;',"'",str(data))
    data = re.sub(r'\s+',' ',str(data))
    data = re.sub('<[^>]&?>','',str(data))
    return data
       
def single_regex(pattern,target_string):
    data = re.findall(pattern,target_string)
    if data != []:
        data = data[0]
    else:
        data = ''
    return data

main_output = "Sl.No"+'\t'+"Generic Name"+'\t'+"Item Weight"+'\t'+"Manufacturer"+'\t'+"Product Title"+'\t'+"Rating"+'\t'+"Number of Ratings"+'\t'+"Bought in Past Month"+'\t'+"MRP"+'\t'+"Discount"+'\t'+"Final Price"+'\n'
with open("MainOutput.txt",'w',encoding="utf-8") as SM:
    SM.write(main_output)
    
error_url_sheet = "URL" + "\n"
with open("ErrorURLSheet.txt",'w',encoding="utf-8") as SM:
    SM.write(error_url_sheet)    
        
driver = webdriver.Chrome()

main_url = driver.get("https://www.amazon.in/")
time.sleep(30)

click_search_bar = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').click()
time.sleep(5)

search_by_product = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("gold coin 24k 1 gram")
time.sleep(5)

click_search_button = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
time.sleep(5)
urls = []

while True:
    
    content = driver.page_source

    content = data_clean(content)

    with open ("Content1.html", 'w', encoding="utf-8") as PC:
        PC.write(content)
    time.sleep(5)

    url_blocks = re.findall(r'(href\=\"[^>]*?\">\s*<h2[^>]*?><[^>]*?>\s*[^>]*?\s*<)',str(content))
    
    for url_block in url_blocks:
        if "sspa/click" not in url_block:
            detailed_page_url = single_regex(r'href\=\"([^>]*?)\"',str(url_block))
            if "Bar" not in url_block:
                detailed_page_url = re.sub('&amp;','&',str(detailed_page_url))
                urls.append(detailed_page_url)
                
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
        click_next = driver.find_element(By.XPATH,"//a[contains(text(),'Next')]").click()
        time.sleep(5)
        
    except:
        break
        
url_count = len(urls)
print(url_count)

num = 0

for url in urls:
    num += 1
    if "http" not in url:
        url_link = "https://www.amazon.in"+url
    try:
        driver.get(url_link)
        detailed_content = driver.page_source
        detailed_content = data_clean(detailed_content)
        with open ("Content2.html", 'w', encoding="utf-8") as PC:
            PC.write(detailed_content)
        product_title = single_regex(r'<title>\s*([^>]*?)\s*<\/title>',str(detailed_content))
        rating = single_regex(r'id\=\"\s*averageCustomerReviews\"\s*data\-asin\=[^>]*?>\s*[\w\W]*?reviewCountTextLinkedHistogram[^>]*?title\=\"\s*([^>]*?)\">',str(detailed_content))
        no_ratings = single_regex(r'CustomerReviewText[^>]*?>\s*(\d+[^>]*?)\s*ratings<\/span>',str(detailed_content))
        bought_past = single_regex(r'\">([^>]*?)\s*bought<\/span>',str(detailed_content))
        mrp = single_regex(r'aok\-offscreen\">\s*M\WR\WP\W\:\s*([^>]*?)\s*<\/span>',str(detailed_content))
        discount = single_regex(r'savingsPercentage\">\s*([^>]*?)\s*<\/span>',str(detailed_content))
        final_price = single_regex(r'a-price-whole\">\s*([^>]*?)\s*<\/span>',str(detailed_content))
        manufacturer = single_regex(r'Manufacturer[^>]*?<\/span>\s*<span>\s*([^>]*?)\s*<\/span>',str(detailed_content))
        item_weight = single_regex(r'Item Weight[^>]*?<\/span>\s*<span>\s*([^>]*?)\s*<\/span>',str(detailed_content))
        generic_name = single_regex(r'Generic Name[^>]*?<\/span>\s*<span>\s*([^>]*?)\s*<\/span>',str(detailed_content))
        
        main_output = str(num)+'\t'+str(generic_name)+'\t'+str(item_weight)+'\t'+str(manufacturer)+'\t'+str(product_title)+'\t'+str(rating)+'\t'+str(no_ratings)+'\t'+str(bought_past)+'\t'+str(mrp)+'\t'+str(discount)+'\t'+str(final_price)+'\n'
        
        with open("MainOutput.txt",'a',encoding="utf-8") as SM:
            SM.write(main_output)
        print("Complted Detailed URL Count: ",str(num))
    
    except:
        print("Error URL: ",str(url_link))
        error_url_sheet = str(url_link) + "\n"
        with open("ErrorURLSheet.txt",'a',encoding="utf-8") as SM:
            SM.write(error_url_sheet) 
print("Data Extraction Complted")

