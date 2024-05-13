from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Start Chrome WebDriver
driver = webdriver.Chrome()

# Open the React todo list application
driver.get("http://localhost:3000/")

# Wait for the page to load
time.sleep(2)

# Execute JavaScript to find the input field and set its value
input_field_script = """
document.querySelector("input[type='text'][placeholder='Enter todo']").value = "Todo 1";
"""
driver.execute_script(input_field_script)

# Execute JavaScript to click the "Add Todo" button

button = driver.find_element(By.XPATH, '//*[@id="Add Todo"]')
button.click()
time.sleep(2)

# add_button_script = """
# document.querySelector("button").click();
# """
# driver.execute_script(add_button_script)

# Wait for the item to be added
time.sleep(2)

# Add 4 more todo items
for i in range(2, 6):
    input_field_script = f"""
    document.querySelector("input[type='text'][placeholder='Enter todo']").value = "Todo {i}";
    """
    driver.execute_script(input_field_script)
    # driver.execute_script(add_button_script)
    button = driver.find_element(By.XPATH, '//*[@id="Add Todo"]')
    button.click()
    # time.sleep(2)
    time.sleep(2)

# Wait for the item to be added
time.sleep(5)


# Find all the delete buttons
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")

# # Delete 3 todo items
# for i in range(3):
#     delete_buttons[i].click()
#     time.sleep(1)

# Delete 3 todo items
for i in range(3):
    if i < len(delete_buttons):  # Check if the index is within the range of delete_buttons
        delete_buttons[i].click()
        time.sleep(2)
# Close the WebDriver session
driver.quit()
