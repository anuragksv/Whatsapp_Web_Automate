from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

country_code = input('Enter the country code of phone numbers (Ex: +91)\n')
ph_no = list(map(str, input('Enter the list of phone numbers\n').split()))
message = input('Enter the Broadcast Message\n')

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

for i in range(len(ph_no)):

    driver.get('https://api.whatsapp.com/send?phone='+str(country_code)+str(ph_no[i]))

    button = driver.find_element_by_xpath('//*[@id="action-button"]')
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(button).click(button).perform()
    
    driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
    time.sleep(6)
    
    message += '\n' 
    textBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textBox.click()
    textBox.send_keys(message)
    time.sleep(2)
