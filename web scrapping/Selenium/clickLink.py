from selenium import webdriver
browser = webdriver.Firefox(executable_path='geckodriver')
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
#<class 'selenium.webdriver.remote.webelement.WebElement'>
linkElem.click() # follows the "Read It Online" link