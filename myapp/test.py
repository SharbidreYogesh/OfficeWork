from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the React todo list application
driver.get("http://localhost:3000/")

# Wait for the page to load
time.sleep(2)

# Loop to add text in the input field and click "Add Todo" button 5 times
for _ in range(5):
    # Find the input field
    input_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter todo']")
    
    # Enter text in the input field
    input_field.clear()  # Clear any existing text
    input_field.send_keys("Test Todo")
    time.sleep(1)
    # Find the "Add Todo" button and click
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Todo']")
    add_button.click()
    
    time.sleep(2)  # Optional: Add a short delay for the item to be added

# Find all the delete buttons
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")

# Delete 3 todo items
for i in range(3):
    if i < len(delete_buttons):  # Check if the index is within the range of delete_buttons
        delete_buttons[i].click()
        time.sleep(2)
# Close the WebDriver session
driver.quit()


