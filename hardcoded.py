from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
DRIVER_PATH = 'C:/Users/Manohar krovvidi/Documents/Tech_Anurag/Git/Whatsapp_Web_Automate/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

###########Edit the code below###############
# add 10 digit phone numbers in the list below separated by ',' 
ph_no = [ 
 ]
###########Edit the code above###############

for i in range(len(ph_no)):

###########Edit Option Available Below###############
# Change the country code (Default = +91) in the line below to send message to international phone numbers.
    driver.get('https://api.whatsapp.com/send?phone=+91'+str(ph_no[i]))
###########Edit Option Available Above###############

    button = driver.find_element_by_xpath('//*[@id="action-button"]')
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(button).click(button).perform()
    
    driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
    time.sleep(8)

###########Edit the code below###############
#add your message here without removing the +'\n'
    message = """Rise & Shine! The Directorate of Student Life is looking forward to interact with the CRs' of various institutes at GITAM. 
    As a part of this endeavour a WhatsApp group has been created. Please Join the group using the link provided below."""
    link = "https://chat.whatsapp.com/IEO2U7Bu6bMIjZJUmrAME9"
###########Edit the code above###############

    message += '\n'
    textBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textBox.click()
    textBox.send_keys(message)
    time.sleep(2)
    textBox.send_keys(link)
    time.sleep(3)
    textBox.send_keys('\n')
    time.sleep(2)