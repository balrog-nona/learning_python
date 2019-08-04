from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox(executable_path='/home/balrog/Dokumenty/Programování/doGIThubu/learning_python/web/'
                                           'geckodriver')
driver.get('https://www.bezfrazi.cz/')
time.sleep(5)

while True:
    try:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(5)
        element = driver.find_element_by_id('read-next-button')
        element.click()
        time.sleep(5)
    except NoSuchElementException:
        break

"""
funguje, ale neni to vubec efektivni. kvuli chybejicim importum mi nefungovaly fce:
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))) 
        - ze pry By. neni definovane
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid'))) - tady taky
a ani toto driver.implicitly_wait(10) # seconds
importy:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

prepsat na efektivni verzi
"""
