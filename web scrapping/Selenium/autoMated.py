#Automated Search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Firefox(executable_path='geckodriver')

browser = webdriver.Firefox(executable_path='C:\\Users\\ujjwal\\AppData\\Local\\Programs\\Python\\Python36\\selenium\\browserdrivers\\geckodriver.exe')

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)


#browser.quit()