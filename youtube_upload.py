from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import config,os

def chrome():
    a=0
    while(a==0):
        try:
            driver = uc.Chrome(use_subprocess=True)
            driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            sleep(1)
            mail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "identifier")))
            mail.send_keys(config.gmail)
            driver.find_element_by_id("identifierNext").click()
            sleep(1)
            passwd = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Passwd")))
            passwd.send_keys(config.password)
            driver.find_element_by_id("passwordNext").click()
            sleep(2)
            driver.get(config.upload_button)
            sleep(1)
            x=config.part
            a+=1

            for i in os.listdir("bot\\Output"):
                driver.find_element_by_css_selector("#content > input[type=file]").send_keys("bot\\Output\\"+i)
                sleep(1)
                notkids = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")))
                notkids.click()
                sleep(1)
                next1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
                next1.click()
                sleep(1)
                next2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
                next2.click()
                sleep(1)
                next3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
                next3.click()
                sleep(1)
                driver.find_element_by_name("PUBLIC").click()
                sleep(1)
                done = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "done-button")))
                done.click()
                print("No: of videos = "+str(x))
                x=x+1
                sleep(5)
                driver.refresh()
                sleep(4)

        except:
            print("Error Occured")