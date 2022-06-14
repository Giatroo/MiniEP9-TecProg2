# Python Standard Libraries
import unittest

# Third Party Libraries
from selenium import webdriver


class TestFundaments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.fundamentus.com.br/index.php")

    def test_empresa_button(self):
        """Tests if the button 'empresa' on the main page redirects the user to
        the right page.
        """
        self.driver.find_element(
            by="xpath", value="/html/body/div[1]/div[1]/div[1]/span/a[1]"
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://www.fundamentus.com.br/buscaavancada.php",
        )

    def test_fii_button(self):
        """Tests if the button 'fii' on the main page redirects the user to
        the right page.
        """
        self.driver.find_element(
            by="xpath", value="/html/body/div[1]/div[1]/div[1]/span/a[2]"
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://www.fundamentus.com.br/fii_buscaavancada.php",
        )

    def test_search(self):
        """Tests if the search bar on the main page redirects the user to the
        page.
        """
        ticker = "PETR4"

        search_bar = self.driver.find_element(
            by="xpath", value='//*[@id="completar"]'
        )
        search_bar.send_keys(ticker)
        search_bar.submit()

        page_ticker = self.driver.find_element(
            by="xpath", value="/html/body/div[1]/div[1]/div[2]/p/strong"
        )

        self.assertEqual(True, ticker in self.driver.title)
        self.assertEqual(page_ticker.text, ticker)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
