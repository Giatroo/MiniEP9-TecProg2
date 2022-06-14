# Python Standard Libraries
import unittest

# Third Party Libraries
from selenium import webdriver


class TestFundaments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.fundamentus.com.br/index.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
