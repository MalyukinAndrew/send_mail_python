def login(driver, credentials):
    selectors = {
        'login_input': 'login',
        'password_input': 'pass',
        'submit_button': '/html/body/div[2]/div[2]/form/input[6]'
    }

    driver.get('https://passport.i.ua/login/')

    login_input = driver.find_element_by_name(selectors['login_input'])
    password_input = driver.find_element_by_name(selectors['password_input'])
    submit_btn = driver.find_element_by_xpath(selectors['submit_button'])

    login_input.send_keys(credentials['login'])
    password_input.send_keys(credentials['password'])
    submit_btn.click()


def open_mail_page(driver):
    driver.get('https://mbox2.i.ua/')

def create_message(driver, recipient):
    selectors = {
        'create_btn': 'make_message',
        'recipient_input': 'to',
        'subject_input': 'subject',
        'message_text': 'text',
        'send_btn': 'send'
    }
    create_btn = driver.find_element_by_class_name(selectors['create_btn'])
    create_btn.click()

    recipient_input = driver.find_element_by_name(selectors['recipient_input'])
    subject_input = driver.find_element_by_name(selectors['subject_input'])
    message_text = driver.find_element_by_id(selectors['message_text'])
    send_btn = driver.find_element_by_name(selectors['send_btn'])

    recipient_input.send_keys(recipient['mail'])
    subject_input.send_keys(recipient['subject'])
    message_text.send_keys(recipient['message'])
    send_btn.click()

def message_was_send (driver, recipient_mail):
    selectors ={
        'last_sended_message': '#mesgList > form .row',
    }
    messages_on_page = driver.find_elements_by_css_selector(selectors['last_sended_message'])
    return recipient_mail in messages_on_page[0].text

def send_message(driver):
    selectors = {
        'sent_mails_btn': '/html/body/div[1]/div[6]/div[2]/div/div/div[2]/div[2]/div[3]/ul/li[2]/a'
    }
    sent_mails_btn = driver.find_element_by_xpath(selectors['sent_mails_btn'])
    sent_mails_btn.click()
