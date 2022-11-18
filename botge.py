import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By

from infos import *

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
driver.implicitly_wait(5)
driver.get('https://cas-usmb.grenet.fr/login?service=https%3A%2F%2Fmoodle.univ-smb.fr%2Flogin%2Findex.php%3FauthCAS%3DCAS')

time.sleep(randint(1,3))

username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)

time.sleep(0.5)

login_button = driver.find_element(By.CSS_SELECTOR, "input[name='submit']")
login_button.click()

time.sleep(randint(1,3))

driver.get('https://moodle.univ-smb.fr/mod/lti/launch.php?id=169573')

time.sleep(randint(1,3))

driver.get('https://exam.global-exam.com/')

time.sleep(randint(1,3))

driver.get(f'https://exam.global-exam.com/library/trainings/exercises/{NUMACT}/activities')

time.sleep(randint(1,3))

entrainements = driver.find_element(By.XPATH, f"//button[contains(text(),'Entraînement {NUMEXO}')]")
entrainements.click()

time.sleep(randint(1,3))

try:
    demarrer = driver.find_element(By.XPATH, "//button[contains(text(),'Démarrer')]")
    demarrer.click()
except:
    print("Déjà démarrer")

time.sleep(randint(1, 3))

for _ in range(29):
    time.sleep(randint(30,80))

    correction = driver.find_element(By.XPATH, "//span[contains(text(), 'Correction')]")
    correction.click()
    time.sleep(randint(1,3))

    bonnereponse = driver.find_element(By.XPATH, "//span[@class='flex font-bold text-success-80']")
    bonnereponse.click()
    time.sleep(randint(1,3))

    correction.click()
    time.sleep(randint(1,3))

    try:
        suivant = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
        suivant.click()
    except:
        try:
            valider = driver.find_element(By.XPATH, "//button[contains(text(), 'Valider')]")
            valider.click()
        except:
            terminer = driver.find_element(By.XPATH, "//button[contains(text(), 'Terminer')]")
            terminer.click()


time.sleep(20)
driver.close()
