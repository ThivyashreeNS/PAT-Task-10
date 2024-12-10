# Task_10.py
# Import necessary libraries for web automation using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Class for URL and basic data
class Data:
   url = "https://www.instagram.com/guviofficial/"

# Class for web-elements locator
class Locators:
    close_button = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]"
    black_ribbon = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/button/span"
    followers = "//span[text()='202K']"
    following = "//span[text()='7']"

class InstaCounts(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def extract_counts(self):
        try:
            # Wait for and close the popup modal
            close = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_button)))
            close.click()
            print("Popup closed")

            # Wait for and close the black ribbon banner
            close_black_ribbon = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.black_ribbon)))
            close_black_ribbon.click()
            print("Black ribbon closed")

            # Wait for and extract followers count
            followers_count_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.followers)))
            followers_count = followers_count_element.text
            print("Followers count:", followers_count)

            # Wait for and extract following count
            following_count_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.following)))
            following_count = following_count_element.text
            print("Following count:", following_count)

            # Return both counts as strings
            return followers_count, following_count

        # Return any exceptions encountered
        except Exception as error:
            print("Error extracting counts:", error)
            return error

    def close_driver(self):
        """Close the browser after extraction"""
        self.driver.quit()