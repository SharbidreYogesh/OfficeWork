from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the HTML file
driver.get("http://127.0.0.1:5500/demo.html")

# Wait for the page to load (adjust sleep time as needed)
time.sleep(12)
