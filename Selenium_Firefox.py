# Gerekli Kütüphanelerin import edilmesi #
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
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
import numpy as np
from selenium.common.exceptions import ElementClickInterceptedException

# path = ph.path_driver2
options = webdriver.FirefoxOptions()
# options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

url = ph.url_proje_firefox
driver.get(url)

wait = WebDriverWait(driver, 20)

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

time.sleep(2)
Abone_Proje_Arsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rowCell0"]/td[3]/a[1]')))
Abone_Proje_Arsivi.click()

time.sleep(1)
Proje_Arsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rowCell5"]/td[3]/a[1]')))
Proje_Arsivi.click()

time.sleep(1)
Name_Sirala = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="browseViewCoreTable"]/tbody/tr[1]/td[3]/a')))
Name_Sirala.click()

time.sleep(1)
I00001_2023 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rowCell1"]/td[3]/a[1]')))
I00001_2023.click()

time.sleep(1)
Name_Sirala_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="browseViewCoreTable"]/tbody/tr[1]/td[3]/a')))
Name_Sirala_1.click()

ProjeNolar = []
ArsivNo = "I00001"
ArsivGrupNo = "I00001-2023"
ProjeNo_Kategory = []
######################################### 
# SAYFA GEÇİŞİ
#########################################
Total_items = int(driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form[3]/div/div/div/table/tbody/tr/td[2]/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]').text.split(" ")[-2])
Total_page = int(np.ceil(Total_items / 25))

print(f"\n I00001-2023 Klasöründe Toplam: {Total_items} Adet .tiff Dosyası Var.")

# X İ DEĞİŞTİR: 
#Buraya sayfanın forunu koy
for x in range(87, (Total_page + 1)):
    print(f"\nToplam {Total_page} Tane Sayfa Var.\n")
    print(f"{x}. Sayfanın Tifflerine Giriliyor...\n")
    if x != 1:
        BirPage_ileri = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#PageNextImg')))
        BirPage_ileri.click()
        time.sleep(3)
        page_count = []
        page_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="browseViewCoreTable"]'))).text.split("\n")
        for y in page_info:
            if y.strip().endswith('.tiff'):
                page = y.strip().replace('.tiff', '')
                page_count.append(page)
        for i in range(0, len(page_count)):
            print(f"\n {x}. Sayfanın, {i+1}. Projesi İşleme Alınıyor. (Proje Nosu: {page_count[i]})")
            time.sleep(1.5)
            try:
                Ilgili_Tiff = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#rowCell{i} > td.browseItemName > a:nth-child(2)')))
                time.sleep(0.5)  # Minik bekleme
                Ilgili_Tiff.click()
            except ElementClickInterceptedException:
                print("⚠️ Element üstü kapanmış. JavaScript ile tıklanıyor...")
                driver.execute_script("arguments[0].click();", Ilgili_Tiff)

            time.sleep(1)
            Properties = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuItem_Properties"]')))
            Properties.click()
            
            time.sleep(0.75)
            get_tiff = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div[6]/div[2]'))).text.split(".")[0]
            
            time.sleep(1)
            Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr[1]/td/form/table/tbody/tr[1]/td/ul/div[2]/li[5]')))
            Categories.click()

            time.sleep(1)
            
            try:
                a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#LLInnerContainer > tbody > tr:nth-child(2) > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2)'))).text
            except:
                print(f"{get_tiff} Belgesinin Kategori Bilgisi Zaten Mevcut !")
                a = ""  # Boş string atayarak devam et

            if a == 'No Categories for this Document.':
                # time.sleep(1)
                original_window = driver.current_window_handle
                Add_Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img')))
                Add_Categories.click()
                # time.sleep(1)
                windows = driver.window_handles
                # time.sleep(1)
                for i in windows:
                    if i != original_window:
                    # Ana pencere olmayan pencereye geçiş yap
                        driver.switch_to.window(i)
                        break

                time.sleep(0.5)
                
                AboneArsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[5]/a')))  
                AboneArsivi.click()

                
                time.sleep(1)
                
                ArsivBilgisi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[10]/td[1]/a')))
                ArsivBilgisi.click()      
                
                # time.sleep(1)
                driver.switch_to.window(original_window)
                
                time.sleep(1)
                ArsivNumarasi = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_2_1"]')))
                ArsivNumarasi.click()
                time.sleep(0.5)
                ArsivNumarasi.send_keys(ArsivNo)
                
                # time.sleep(1)
                ArsivGrup = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_3_1"]')))
                ArsivGrup.click()
                time.sleep(0.5)
                ArsivGrup.send_keys(ArsivGrupNo)
                
                # time.sleep(1)
                Apply = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[2]')))
                Apply.click()
                print(f"{get_tiff} Proje Belgesinin Arşiv Bilgisi Eklendi.")
                time.sleep(2)

                Add_Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img')))
                Add_Categories.click()

                # time.sleep(1)
                windows = driver.window_handles

                for i in windows:
                    if i != original_window:
                    # Ana pencere olmayan pencereye geçiş yap
                        driver.switch_to.window(i)
                        break

                time.sleep(1)  

                AboneArsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[5]/a')))  
                AboneArsivi.click()

                
                time.sleep(1)

                ProjeDoküman_Bilgisi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[20]/td[1]/a')))
                ProjeDoküman_Bilgisi.click()

                time.sleep(2.5)
                driver.switch_to.window(original_window)
                time.sleep(1)

                # time.sleep(1)  
                try:
                    ProjeNo = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div[6]'))).text.split(".")[0]
                    EskiProjeNo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_2_1"]')))
                    EskiProjeNo.click()
                    EskiProjeNo.send_keys(ProjeNo)
                    # time.sleep(1)
                    ProjeNolar.append(ProjeNo)
                    print(f"Proje No: {ProjeNo} başarıyla listeye eklendi")
                except Exception as e:
                    print(f"Hata oluştu: {str(e)}")

                time.sleep(1)

                YeniProjeNo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_3_1"]')))
                YeniProjeNo.click()
                YeniProjeNo.send_keys(ProjeNo)
                
                time.sleep(1) 

                BalyaNo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_4_1"]')))
                BalyaNo.click()
                BalyaNo.send_keys(ArsivNo)

                time.sleep(1) 

                ProjeDoküman_Tipi_Secim = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[7]/td[2]/select/option[2]')))
                ProjeDoküman_Tipi_Secim.click()

                time.sleep(0.75)

                ProjeGuncel_Durum = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[9]/td[2]/select/option[2]')))
                ProjeGuncel_Durum.click()

                time.sleep(0.75)

                Apply = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[2]')))
                Apply.click()
                print(f"{get_tiff} Proje Belgesinin Proje Doküman Bilgisi Eklendi.")
                time.sleep(2)

                Submit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[1]')))
                Submit.click()
                print(f"{get_tiff} Projesinin Kategori Bilgileri Eklendi ve Submit Edildi !")
                time.sleep(2.5)

            else:
                ProjeNo_Kategory_Var = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div[6]'))).text.split(".")[0]
                ProjeNo_Kategory.append(ProjeNo_Kategory_Var)
                print(f"{ProjeNo_Kategory_Var} Numaralı Proje, 'Kategori Bilgisi Olanlar'a Kaydediliyor.")
                time.sleep(2)
                Klasore_Donus = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="80455978_0"]')))
                Klasore_Donus.click()
    else:
        page_count = []
        page_info = driver.find_element(By.XPATH, '//*[@id="browseViewCoreTable"]').text.split("\n")
        for y in page_info:
            if y.strip().endswith('.tiff'):
                page = y.strip().replace('.tiff', '')
                page_count.append(page)
        for i in range(0, len(page_count)):
            print(f"\n {x}. Sayfanın, {i+1}. Projesi İşleme Alınıyor. (Proje Nosu: {page_count[i]})")
            time.sleep(1)
            #rowCell15 > td.browseItemName > a:nth-child(2)
            Ilgili_Tiff = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#rowCell{i} > td.browseItemName > a:nth-child(2)')))
            Ilgili_Tiff.click()

            time.sleep(1)
            Properties = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuItem_Properties"]')))
            Properties.click()

            get_tiff = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div[6]/div[2]').text.split(".")[0]
            
            time.sleep(1)
            Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr[1]/td/form/table/tbody/tr[1]/td/ul/div[2]/li[5]')))
            Categories.click()

            time.sleep(1.25)

            
            try:
                a = driver.find_element(By.CSS_SELECTOR, '#LLInnerContainer > tbody > tr:nth-child(2) > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2)').text
            except:
                print(f"{get_tiff} Belgesinin Kategori Bilgisi Zaten Mevcut !")
                a = ""  # Boş string atayarak devam et

            if a == 'No Categories for this Document.':
                time.sleep(1)
                original_window = driver.current_window_handle
                Add_Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img')))
                Add_Categories.click()
                time.sleep(1)
                windows = driver.window_handles
                time.sleep(1)
                for i in windows:
                    if i != original_window:
                    # Ana pencere olmayan pencereye geçiş yap
                        driver.switch_to.window(i)
                        break

                time.sleep(1)
                
                AboneArsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[5]/a')))  
                AboneArsivi.click()

                
                time.sleep(2)
                
                ArsivBilgisi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[10]/td[1]/a')))
                ArsivBilgisi.click()      
                
                time.sleep(1)
                driver.switch_to.window(original_window)
                
                time.sleep(1)
                ArsivNumarasi = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_2_1"]')))
                ArsivNumarasi.click()
                time.sleep(1)
                ArsivNumarasi.send_keys(ArsivNo)
                
                time.sleep(1)
                ArsivGrup = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_3_1"]')))
                ArsivGrup.click()

                time.sleep(1)
                ArsivGrup.send_keys(ArsivGrupNo)
                
                time.sleep(1)
                Apply = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[2]')))
                Apply.click()
                print(f"{get_tiff} Proje Belgesinin Arşiv Bilgisi Eklendi.")
                time.sleep(3)

                Add_Categories = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LLInnerContainer"]/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img')))
                Add_Categories.click()

                time.sleep(1)
                windows = driver.window_handles

                for i in windows:
                    if i != original_window:
                    # Ana pencere olmayan pencereye geçiş yap
                        driver.switch_to.window(i)
                        break

                time.sleep(1)  

                AboneArsivi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[5]/a')))  
                AboneArsivi.click()

                
                time.sleep(2)

                ProjeDoküman_Bilgisi = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[20]/td[1]/a')))
                ProjeDoküman_Bilgisi.click()

                time.sleep(1)
                driver.switch_to.window(original_window)

                time.sleep(1)  
                try:
                    ProjeNo = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div[6]').text.split(".")[0]
                    EskiProjeNo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_2_1"]')))
                    EskiProjeNo.click()
                    EskiProjeNo.send_keys(ProjeNo)
                    time.sleep(1)
                    ProjeNolar.append(ProjeNo)
                    print(f"Proje No: {ProjeNo} başarıyla listeye eklendi")
                except Exception as e:
                    print(f"Hata oluştu: {str(e)}")

                time.sleep(1)

                YeniProjeNo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_3_1"]')))
                YeniProjeNo.click()
                YeniProjeNo.send_keys(ProjeNo)
                
                time.sleep(1) 

                BalyaNo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_1_1_4_1"]')))
                BalyaNo.click()
                BalyaNo.send_keys(ArsivNo)

                time.sleep(1) 

                ProjeDoküman_Tipi_Secim = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[7]/td[2]/select/option[2]')))
                ProjeDoküman_Tipi_Secim.click()

                time.sleep(1)

                ProjeGuncel_Durum = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[9]/td[2]/select/option[2]')))
                ProjeGuncel_Durum.click()

                time.sleep(1)

                Apply = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[2]')))
                Apply.click()
                print(f"{get_tiff} Proje Belgesinin Proje Doküman Bilgisi Eklendi.")
                time.sleep(1.5)

                Submit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[1]')))
                Submit.click()
                print(f"{get_tiff} Projesinin Kategori Bilgileri Eklendi ve Submit Edildi !")
                time.sleep(2)

            else:
                
                ProjeNo_Kategory_Var = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div[6]').text.split(".")[0]
                ProjeNo_Kategory.append(ProjeNo_Kategory_Var)
                print(f"{ProjeNo_Kategory_Var} Numaralı Proje, 'Kategori Bilgisi Olanlar'a Kaydediliyor.")
                time.sleep(2)
                Klasore_Donus = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="80455978_0"]')))
                Klasore_Donus.click()


print(f"\nİşlem Tamamlandı!")
print(f"Toplam işlenen proje sayısı: {len(ProjeNolar)}")
print(f"Kategori bilgisi önceden mevcut olan proje sayısı: {len(ProjeNo_Kategory)}")

