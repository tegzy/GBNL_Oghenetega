from _ast import Assert

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.testsite.com/")

driver.find_element_by_id("ID").send_keys("username")
driver.find_element_by_id("ID").send_keys("password")
driver.find_element_by_id("loginButton").click()


# click on the specific button four times and assert the success message is displayed
driver.find_element_by_id("a_specific_button").click()
driver.find_element_by_id("a_specific_success_message").is_displayed()

driver.find_element_by_id("a_specific_button").click()
driver.find_element_by_id("a_specific_success_message").is_displayed()

driver.find_element_by_id("a_specific_button").click()
driver.find_element_by_id("a_specific_success_message").is_displayed()

driver.find_element_by_id("a_specific_button").click()
driver.find_element_by_id("a_specific_success_message").is_displayed()

Assert.assertTrue(driver.find_element_by_id("a_specific_button").isEnabled())