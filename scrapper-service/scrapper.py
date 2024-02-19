import time

import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from locators import lidl_locators
from datamodels import datamodels


def driver_setup() -> selenium.webdriver.Chrome:
	chrome_options = Options()
	# chrome_options.add_argument('--headless')
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_experimental_option("prefs", {"translate_whitelists": {"de": "en"}, "translate": {"enabled": "true"}})

	driver = selenium.webdriver.Chrome(options=chrome_options)
	time.sleep(15)  # Adding this delay makes the translation work for some reason?

	return driver

# def extract_weight(raw_weight_string: str):
# 	if raw_weight_string.split(' ') > 1:
# 		return


def main():
	# try:
	driver = driver_setup()
	driver.get(lidl_locators.VEGETABLES_URL_LIDL)

	cookies_popup = driver.find_element_by_xpath(
		lidl_locators.REJECT_COOKIES_BUTTON_XPATH
	)

	WebDriverWait(driver, 20).until(
		expected_conditions.visibility_of_element_located(
			(By.XPATH, lidl_locators.REJECT_COOKIES_BUTTON_XPATH)
		)
	)
	cookies_popup.click()

	try:
		while True:
			load_more_button = driver.find_element_by_xpath(
				lidl_locators.LOAD_MORE_BUTTON_LIDL_XPATH
			)
			WebDriverWait(driver, 20).until(
				expected_conditions.visibility_of_element_located(
					(By.XPATH, lidl_locators.LOAD_MORE_BUTTON_LIDL_XPATH)
				)
			)
			time.sleep(1)
			if load_more_button.is_displayed():
				location = load_more_button.location_once_scrolled_into_view
				time.sleep(1)
				# location = load_more_button.location_once_scrolled_into_view
				# print(f'location: {location}')
				ac = ActionChains(driver)
				ac.move_to_element(load_more_button).click().perform()

	except NoSuchElementException:
		print("no more elements")

	items = driver.find_elements_by_xpath(
		lidl_locators.LIST_ITEM_DETAILS_CONTAINER_XPATH
	)

	links = driver.find_elements_by_xpath(
		lidl_locators.LIST_ITEM_DETAILS_ITEM_LINK_XPATH
	)
	# .get_attribute('href'))
	names = driver.find_elements_by_xpath(
		lidl_locators.LIST_ITEM_DETAILS_ITEM_NAME_XPATH
	)
	prices = driver.find_elements_by_xpath(
		lidl_locators.LIST_ITEM_DETAILS_ITEM_PRICE_XPATH
	)
	weights = driver.find_elements_by_xpath(
		lidl_locators.LIST_ITEM_DETAILS_ITEM_QUANTITY_XPATH
	)

	for index, item in enumerate(items):
		vegetable = datamodels.Vegetable(
			names[index].text,
			prices[index].get_attribute("content"),
			weights[index].text,
		)

		print(f"weight: {names}")
	# vegetable = datamodels.Vegetable(name, price, )

	print(f"items: {len(items)}")

	driver.close()


# except Exception as exception:
# 	print(f'Exception: {exception}')
# 	driver.close()


if __name__ == "__main__":
	main()
