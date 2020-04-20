# Import Selenium dependencies
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Import Beautiful Soup Dependencies
from bs4 import BeautifulSoup
from csv import writer

# Load in Chrome Driver and Navigate to Shop Lowe's Foods
driver = webdriver.Chrome('./driver/chromedriver')
driver.get("https://shop.lowesfoods.com/")

# Make sure driver waits up to 10 seconds for page to load
driver.implicitly_wait(10)

# Exit out of promotional if it appears
try:
    rewards_close = driver.find_element_by_id("loyalty-onboarding-dismiss")
    rewards_close.click()
except NoSuchElementException:
    print("Shopping reward locator was not found on page")

# Exit out of store locator if it appears
try:
    location_close = driver.find_element_by_id("shopping-selector-parent-process-modal-close-click")
    location_close.click()
except NoSuchElementException:
    print("Shopping location locator was not found on page")

# Go to Beer and Wine section
beer_wine_label = driver.find_element_by_id("nav-main-shop-category-3697")
beer_wine_label.click()

# Go to Beer section
domestic = driver.find_element_by_id("catalog-category-3714")
domestic.click()

# Driver will implicitly wait until the page has loaded list elements before running soup
driver.find_element_by_class_name('cell-title-text')

# Get the HTML for the current Beer page and initialize beautiful Soup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find all Beer and Price listings in the first page
posts = soup.find_all(class_='cell-wrapper ng-scope')

# Open csv file for beer name and price storage
with open('beerList.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Price']
    csv_writer.writerow(headers)

    # Save all beer names and prices in csv file
    for post in posts:
        name = post.find(class_='cell-title-text').get_text()
        price = post.find(class_='product-prices').get_text().replace('\n', '')
        csv_writer.writerow([name, price])

driver.close()
