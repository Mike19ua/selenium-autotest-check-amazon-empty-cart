import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_AmazonCart:

    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/Dell/PycharmProjects/selenium/chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com/')

    def test_empty_cart(self):
        self.driver.find_element(By.ID, 'nav-cart').click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
        expected_text = 'Your Amazon Cart is empty'
        assert actual_text == expected_text, f"Error.Expected_text: '{expected_text}', but actual text: '{actual_text}'"

    def teardown_method(self):
        self.driver.quit()
