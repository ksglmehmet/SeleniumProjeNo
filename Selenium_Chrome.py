# Gerekli Kütüphanelerin import edilmesi #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
# Klavye komutlarını verebilmek için.
from selenium.webdriver.support.ui import WebDriverWait 
#time.sleep yerine, belirli bir elemanın görünür hale gelmesiyle işlem yapmasını sağlamak için.
from selenium.webdriver.support import expected_conditions as EC 
#time.sleep yerine, belirli bir elemanın görünür hale gelmesiyle işlem yapmasını sağlamak için.
import time
import path as ph
import pandas as pd
import os

path = ph.path_driver
service = Service(path)
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument('--disable-notifications')
# options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service = service, options = options)

url = ph.url_proje
driver.get(url)

wait = WebDriverWait(driver, 10)

time.sleep(1)
UserName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="otds_username"]')))
UserName.click()
UserName.send_keys(ph.User_Name)

time.sleep(1)
Password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="otds_password"]')))
Password.click()
Password.send_keys(ph.User_Password)

time.sleep(1)
Signin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]')))
Signin.click()

time.sleep(1.5)
Abone_Proje_Arsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rowCell0"]/td[3]/a[1]')))
Abone_Proje_Arsivi.click()

time.sleep(1.5)
Proje_Arsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rowCell5"]/td[3]/a[1]')))
Proje_Arsivi.click()

time.sleep(1.5)
Name_Sirala = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="browseViewCoreTable"]/tbody/tr[1]/td[3]/a')))
Name_Sirala.click()

time.sleep(1.5)
I00001_2023 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rowCell1"]/td[3]/a[1]')))
I00001_2023.click()

time.sleep(1.5)
Name_Sirala_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="browseViewCoreTable"]/tbody/tr[1]/td[3]/a')))
Name_Sirala_1.click()

time.sleep(1.5)
Functions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rowCell1 > td.browseItemName > a:nth-child(2)')))
Functions.click()

time.sleep(1.5)
Properties = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuItem_Properties"]')))
Properties.click()

time.sleep(1)
Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr[1]/td/form/table/tbody/tr[1]/td/ul/div[2]/li[5]')))
Categories.click()

time.sleep(1.5)
a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#LLInnerContainer > tbody > tr:nth-child(2) > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2)'))).text
if a == 'No Categories for this Document.':
    original_window = driver.current_window_handle
    Add_Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img')))
    Add_Categories.click()
    time.sleep(1)
    windows = driver.window_handles
    time.sleep(1.5)
    for i in windows:
        if i != original_window:
        # Ana pencere olmayan pencereye geçiş yap
            driver.switch_to.window(i)
            break
    # driver.close()
    driver.page_source
    wait.until(EC.element_to_be_clickable((By.ID, 'functionMenuParent')))
    time.sleep(2)
    AboneArsivi = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[5]/a')))  
    AboneArsivi.click      
c = driver.find_elements(By.CSS_SELECTOR, '#targetbrowseview > tbody > tr:nth-child(4) > td.browseItemName > a')
d = driver.find_element(By.XPATH, '//*[@id="main-frame-error"]')
b = driver.current_window_handle

# //*[@id="menuItem_Properties"]
# //*[@id="menuItem_Properties"]
# #menuItem_Properties
# menuItem_Properties


# #rowCell0 > td.browseItemName > a:nth-child(2)

# driver.find_element(By.CSS_SELECTOR, '#rowCell0 > td.browseItemName > a.browseItemNameContainer').text
# driver.find_element(By.CSS_SELECTOR, '#rowCell1 > td.browseItemName > a.browseItemNameContainer').text





# # time.sleep(3)
# # driver.quit()

