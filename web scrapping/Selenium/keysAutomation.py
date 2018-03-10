import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='geckodriver')
browser.get('https://www.msn.com')

htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
time.sleep(5)
htmlElem.send_keys(Keys.HOME)
#browser.close()

'''
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
Keys.ENTER, Keys.RETURN
Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
Keys.F1, Keys.F2,..., Keys.F12, Keys.TAB

browser.back()
browser.forward()
browser.refresh()
browser.quit()
'''
