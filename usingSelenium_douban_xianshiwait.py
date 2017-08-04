from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome("chromedriver.exe")

browser = webdriver.Firefox()

browser.set_page_load_timeout(10)

try:
    browser.get('https://read.douban.com/kind/105')
except Exception as e:
    print(e)

for i in range(3):
    try:
        next = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.next>a')))
        titles = browser.find_elements_by_css_selector('.title>a')
        titles_text = [t.text for t in titles]
        print(titles_text)

        next.click()
    except Exception as e:
        print(e)

browser.close()
