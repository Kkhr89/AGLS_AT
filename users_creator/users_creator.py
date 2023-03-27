import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from testdata import *


# Function to identify total users amount:
def row_count():
    count = 0
    wb = openpyxl.load_workbook('users.xlsx')
    sheet = wb.active
    for row in sheet.iter_rows():
        if all(cell.value is None for cell in row):
            break
        count += 1
    return count


# Function to create dictionary with all the users in .xlsx:
def users_parser():
    dict_users = dict()
    wb = openpyxl.load_workbook('users.xlsx')
    sheet = wb.active
    i = 1
    for row in sheet.iter_rows(min_row=2, values_only=True):
        first_name, last_name, email = row
        dict_users[f'first_name_{i}'] = first_name
        dict_users[f'last_name_{i}'] = last_name
        dict_users[f'email_{i}'] = email
        i += 1
    return dict_users

# Function to create all users from .xlsx in AgileS app:
def user_creator():
    for i in range(1, row_count()):
        name = users_parser()[f'first_name_{i}']
        surname = users_parser()[f'last_name_{i}']
        email = users_parser()[f'email_{i}']
        browser = webdriver.Chrome(ChromeDriverManager().install())
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up"))).click()
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter First Name']").send_keys(name)
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Last Name (Optional)']").send_keys(surname)
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Your Email']").send_keys(email)
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm Password']").send_keys('Godfather1989!')
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msglist-message:first-child'))).click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))
        browser.quit()
        print(f'User {name} {surname}, email: {email} was created')
    print(f'{row_count() - 1} Users were created successfully')

# launch User creator:
user_creator()
