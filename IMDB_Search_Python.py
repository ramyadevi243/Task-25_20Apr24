from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time


# Create a class called IMDB
class IMDB:
    # # Calling constructor with parameter url
    def __init__(self, url):
        self.url = url

    # Method to initiate Chrome webdriver, maximize window and get the specified URL
    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)


    def static_pause(self, seconds):
        start_time = time.time()
        while (time.time() - start_time) < seconds:
            pass

    # Method to scroll down by pixels
    def scroll_window_down(self, pixels):
        script = f"window.scrollBy(0, {pixels});"
        self.driver.execute_script(script)

    # Method to fill in name search
    def name_filter(self):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn'][text()='Name']")))
        name_input.click()

        name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name-text-input']")))
        name_field.send_keys("DiCaprio")
        print("Searched for name: DiCaprio")

    # Method to fill in birthdate
    def birth_date(self):
        birth = self.driver.find_element(By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn'][text()='Birth date']")
        birth.click()

        date = self.driver.find_element(By.XPATH, "//input[@name='birth-date-start-input']")
        date.send_keys("11-11-1974")
        print("Birth Date: 11 November 1974")

    # Method to select Awards and Recognition
    def awards_recognition(self):
        awards_select_elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn'][text()='Awards & recognition']")))
        awards_select_elem.click()

        oscar = self.driver.find_element(By.XPATH, "//*[@id='accordion-item-awardsAccordion']/div/section/button[4]")
        oscar.click()
        print("Awards and Recognition: Best Actor Oscar-Winning")

    # Method to search results
    def see_result(self):
        result = self.driver.find_element(By.XPATH, "//span[@class='ipc-btn__text'][text()='See results']")
        result.click()
        print("Search Successful for Leonardo DiCaprio")

    def assert_search(self):
        try:
            assert "dicaprio" in self.driver.current_url.lower()
        except AssertionError as e:
            raise AssertionError("Search Not Successful") from e

    # Method to close the browser
    def close(self):
        self.driver.quit()
        print("Browser closed successfully")


# Executing the main method
if __name__ == "__main__":

    # Passing the value to the url
    url = "https://www.imdb.com/search/name/"

    # Created an object for class IMDB
    imdb = IMDB(url)

    # Calling all methods
    imdb.start()
    imdb.scroll_window_down(300)
    imdb.static_pause(1)
    imdb.name_filter()
    imdb.scroll_window_down(300)
    imdb.static_pause(1)
    imdb.birth_date()
    imdb.scroll_window_down(200)
    imdb.static_pause(1)
    imdb.awards_recognition()
    imdb.see_result()
    imdb.assert_search()
    imdb.close()
