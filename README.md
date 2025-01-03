# Amazon_Gold_Coin_Selenium
Data Extraction from Amazon Gold Coin using Python and Selenium

Gold Coin Search in Amazon Website using Python Selenium
Developer: MARUTHACHALAM S Project Title: Gold Coin Search in Amazon Website using Python Selenium Date: 03.01.2025 Version: 1

Description
This project involves web scraping the Amazon website to search for gold coins of 24K 1 gram and extracting details such as product title, rating, number of ratings, MRP, discount, final price, manufacturer, item weight, and generic name. The extracted data is then saved into a text file.

Requirements
Python 3.x

Selenium

Requests

ChromeDriver

Installation
Install Python: Ensure you have Python 3.x installed.

Install Required Libraries:
pip install selenium requests

Download ChromeDriver:
Download the appropriate version of ChromeDriver from here.

Run the Script:
python Amazon_Gold_Coin_Selenium.py

Script Explanation
data_clean: Cleans HTML content by removing special characters and HTML tags.

single_regex: Extracts the first match of a regex pattern from a target string.

Main Script:

Opens Amazon website.

Searches for "gold coin 24k 1 gram".

Iterates through the search results, extracting URLs for each product.

Extracts detailed information from each product page.

Saves the extracted data into MainOutput.txt and logs any errors in ErrorURLSheet.txt.

Output Files
MainOutput.txt: Contains the extracted product details in tab-separated format.

ErrorURLSheet.txt: Logs URLs that encountered errors during the extraction process.

Example Output (MainOutput.txt)
Sl.No  Generic Name  Item Weight  Manufacturer  Product Title  Rating  Number of Ratings  Bought in Past Month  MRP  Discount  Final Price
1      Example Name  1 gram       Example Man.  Example Title  4.5     100                20                    ₹5000 ₹10       ₹4500
...
Additional Information
Error Handling: URLs that cause errors during extraction are logged in ErrorURLSheet.txt.

Scrolling and Pagination: The script scrolls down to load more products and clicks the "Next" button to navigate through pages.

Author
MARUTHACHALAM S
