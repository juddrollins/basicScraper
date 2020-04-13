from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./driver/chromedriver')
driver.get("https://shop.lowesfoods.com/")

driver.implicitly_wait(10)

try:
    rewards_close = driver.find_element_by_id("loyalty-onboarding-dismiss")
    rewards_close.click()
except NoSuchElementException:
    print("Shopping reward locator was not found on page")

try:
    location_close = driver.find_element_by_id("shopping-selector-parent-process-modal-close-click")
    location_close.click()
except NoSuchElementException:
    print("Shopping location locator was not found on page")

beer_wine_label = driver.find_element_by_id("nav-main-shop-category-3697")
beer_wine_label.click()

domestic = driver.find_element_by_id("catalog-category-3714")
domestic.click()

if



driver.close()