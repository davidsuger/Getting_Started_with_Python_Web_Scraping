from selenium import webdriver
from selenium.webdriver.support import ui

# browser = webdriver.Chrome("chromedriver.exe")

browser = webdriver.Firefox()

browser.set_page_load_timeout(10)
browser.implicitly_wait(5)
try:
    browser.get('https://read.douban.com/kind/105')
except Exception as e:
    print(e)

for i in range(3):
    titles=browser.find_elements_by_css_selector('.title>a')
    titles_text=[t.text for t in titles]
    print(titles_text)
    next=browser.find_element_by_css_selector('.next>a')
    try:
        next.click()
    except Exception as e:
        print(e)

