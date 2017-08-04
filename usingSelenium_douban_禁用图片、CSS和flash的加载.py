from selenium import webdriver

# browser = webdriver.Chrome("chromedriver.exe")

firefoxProfile=webdriver.FirefoxProfile()
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
firefoxProfile.set_preference('permissions.default.image', 2)
browser = webdriver.Firefox(firefoxProfile)

browser.get('https://read.douban.com/kind/105')
for i in range(10):
    titles=browser.find_elements_by_css_selector('.title>a')
    titles_text=[t.text for t in titles]
    print(titles_text)
    next=browser.find_element_by_css_selector('.next>a')
    next.click()

