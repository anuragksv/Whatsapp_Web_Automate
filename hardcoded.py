from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

DRIVER_PATH = 'C:/Users/anura/Documents/Python/Whatsapp_Web_Automate/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

###########Edit the code below###############
# add 10 digit phone numbers in the list below separated by ','
ph_no = [
8500087595,
6303764073]

###########Edit the code above###############

for i in range(len(ph_no)):

    ###########Edit Option Available Below###############
    # Change the country code (Default = +91) in the line below to send message to international phone numbers.
    driver.get('https://api.whatsapp.com/send?phone=+91'+str(ph_no[i]))
###########Edit Option Available Above###############

    button = driver.find_element_by_xpath('//*[@id="action-button"]')
    driver.implicitly_wait(3)
    ActionChains(driver).move_to_element(button).click(button).perform()

    driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
    time.sleep(7)

###########Edit the code below###############
# add your message here without removing the +'\n'
    message = """Greetings from Genesis! I'm Anurag - Mentor of SIG Genesis, We would like to have a word with you about being our prospective clients for your website. Since Joel Sir has stated giving him the 250-300 words description is sufficient. Thank You.\n"""
###########Edit the code above###############

    textBox = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textBox.click()
    time.sleep(1)
    textBox.send_keys(message)
    time.sleep(3)
