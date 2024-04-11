from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
username = os.environ.get('github_username')
password = os.environ.get('github_password')

browser = webdriver.Chrome()


browser.get(f"https://github.com/{username}?tab=repositories")


# Extract repository names and create a list
all_repository_names = []

previous_repo_count = 0


while True:
    # Scroll to the bottom of the page to look for all the repositories and wait untill all the repositories are read
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  

    repository_elements = browser.find_elements(By.CSS_SELECTOR, f"a[href^='/{username}/']")
    
    
    all_repository_names.extend([element.text for element in repository_elements])


    next_button = browser.find_elements(By.CSS_SELECTOR, "span.next_page[aria-disabled='true']")
    
    
    if next_button:
        break 
    
    next_button = browser.find_element(By.XPATH, "//a[@rel='next']")
    next_button.click()
    

print(all_repository_names)
if "JavaScript-Core-1-Coursework-Week4-London10" in all_repository_names:
    print("Found")
else:
    print("Not found")

browser.quit() 





