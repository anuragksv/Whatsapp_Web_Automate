# Brief
  The project uses selenium web scrapper to send direct messages to known and unknown contacts though whatsapp web.

# Pre-Requisites
  1. Python 3.X
  2. Chrome-Driver for your google chrome version (85.x in repo). Read more about it here - (https://chromedriver.chromium.org/)
  3. Selenium Framework - *pip install selenium*

# Versions Available
  The project contains two versions. Where,
  1. hardcoded.py - Changes to the code have to be made in two mandatory and one optional section. 
     + First section is the list of phone numbers. Note that the phone numbers need to be 10-digits without any spaces or hiphes in middle.
     + Second section is country code of the number which is by default set to +91 India.
     + Third section is the message section, where you replace the given same message with your broadcast message.
    
  2. cli.py - Three sets of input have to be given. Which are,
     + Enter the country code of phone numbers (Ex: +91) 
     + Enter the list of phone numbers - *Enter the numbers with spaces between each 10-digit input. Upon clicking Enter, Control moves on to next input statement.*
     + Enter the Broadcast Message - Enter your message here without having it as a multiline input. To send multiple messages use '\n' in your text.

# Execution Instructions
  1. Upon execuiting each version of script., the automated testing chrome window pops up.
  2. The first time the window opens, we will be asked to scan the QR code on screen though our mobile whatsapp application for login. *We get a 6 seconds time span to complete this step*
  3. Messages to each contact takes ~ 10 seconds
  4. Upon completion of the process the browser automatically closes. 

### NOTE
  1. The project is still in (Beta) stages and further refining of code through exception handling etc., will be done in later updates.
  2. More efficient ways of dealing with the task at hand are being considered as well. 
        
