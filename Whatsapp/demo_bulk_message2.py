from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_xpath('//div[contains(@class,"_1hRBM")]/div[2]')

for i in range(count):
    this_msg = msg + str(i+1)
    msg_box.send_keys(this_msg)
    driver.find_element_by_xpath('//div[contains(@class,"_3qpzV")]/button').click()
