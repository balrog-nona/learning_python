from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import path_to_geckodriver

driver = webdriver.Firefox(executable_path=path_to_geckodriver.path)

driver.get('https://www.bezfrazi.cz/')
driver.implicitly_wait(4)

cookies = driver.find_element_by_id('cookies-agree-button')
cookies.click()
driver.implicitly_wait(4)

iterace = 0
while True:
    try:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        driver.implicitly_wait(2)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'read-next-button')))
        element.click()
        iterace += 1
        driver.implicitly_wait(2)
    except TimeoutException:
        print('Pocet clicku: {}'.format(iterace))
        break
