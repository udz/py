from selenium import webdriver

#browser = webdriver.Chrome(executable_path="chromedrv")
browser = webdriver.Firefox(executable_path="geckodriver")
browser.get('http://seleniumhq.org/')
'''
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')



capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False
binary = FirefoxBinary(r'/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

'''
