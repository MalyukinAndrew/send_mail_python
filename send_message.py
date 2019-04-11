import sys
from functions import *
from selenium import webdriver

credentials = {'login': sys.argv[1], 'password': sys.argv[2]}
recipient = {'mail': sys.argv[1], 'subject': 'automation', 'message': 'Hello from selenium'}

driver = webdriver.Chrome('E:\PyProject\TestMail\chromedriver.exe')

login(driver, credentials)

open_mail_page(driver)

create_message(driver, recipient)

send_message(driver)

if message_was_send(driver, recipient['mail']):
    print('Mail was sent')
else:
    print('Message not sent')

driver.quit()