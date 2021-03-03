import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_something(self):
        self.browser.get("https://yandex.ru/")
        news = self.browser.find_elements(By.CLASS_NAME, 'news__item-content')
        for item in news:
            print(item.text)

        search_field = self.browser.find_element(By.ID, "text")
        search_field.send_keys("С 8 марта, Женька!!!")
        search_field.send_keys(Keys.RETURN)

        self.browser.find_element(By.LINK_TEXT, "С 8 марта, женька!!! — смотрите картинки").click()

        self.browser.find_element(By.LINK_TEXT, "С 8 марта, женька!!! — смотрите картинки").click()
        # self.assertTrue(element.is_displayed())
        # element.click()
        # pricing_link = self.browser.find_element(By.XPATH, '//a[text()="Pricing"]')
        # self.assertTrue(pricing_link.is_displayed())
        # pricing_link.click()

    def tearDown(self) -> None:
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
