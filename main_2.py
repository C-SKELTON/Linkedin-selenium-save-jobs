from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")
chrome_driver_path = Service("C:/Users/conno/chrome_driver/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)
id_ = os.getenv("LN_Email")
pass_ = os.getenv("LN_Password")

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3048378073&f_AL=true&f_JT=F&f_TPR=r2592000&geoId=103644278&keywords=sql%20analyst&location=United%20States")
driver.maximize_window()
time.sleep(5)


sign_in_btn = driver.find_element(By.LINK_TEXT,'Sign in')
#sign_in_btn = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_btn.click()

login_id = driver.find_element(By.ID, 'username') #Your Username
login_id.send_keys(id_)

password_id = driver.find_element(By.ID, 'password')
password_id.send_keys(pass_)

#login_btn = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
login_btn = driver.find_element(By.CSS_SELECTOR,'.btn__primary--large')
login_btn.click()

chat_minimize = driver.find_element(By.CSS_SELECTOR, '.msg-overlay-bubble-header__details')
chat_minimize.click()

jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
save_button = driver.find_element(By.CSS_SELECTOR,".jobs-save-button")
print(len(jobs_list))

search_result = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div")
scroll_cor = 100
for n in range(25):
    driver.execute_script(f"arguments[0].scrollTo(0, {scroll_cor})", search_result)
    scroll_cor += 100
    time.sleep(0.5)

for job in jobs_list:
    jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    job.click()
    time.sleep(2)
    save_button.click()
    time.sleep(2)
driver.quit()