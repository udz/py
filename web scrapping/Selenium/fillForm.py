from selenium import webdriver

browser = webdriver.Firefox(executable_path='geckodriver')
browser.get('http://202.166.194.123:8383')

msisdn = browser.find_element_by_id('txtMsisdn')
msisdn.send_keys('9808249920')
pwd = browser.find_element_by_id('txtPIN')
pwd.send_keys('1111')

login = browser.find_element_by_id('lnkLogin')
login.click()


#browser.close()