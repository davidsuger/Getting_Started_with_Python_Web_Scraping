from selenium import webdriver

# browser = webdriver.Chrome("chromedriver.exe")
browser = webdriver.Firefox()

browser.get('http://www.baidu.com')
# browser.execute_script("alert('hello')")
input=browser.find_element_by_css_selector('#kw')
input.send_keys('眼睛蛇')
browser.save_screenshot('test.png')

# browser.set_page_load_timeout(5)
browser.get('http://reddit.com')
for i in range(3):
    titles=browser.find_elements_by_css_selector('a.title')
    # for t in titles:
    #     print(t.text)
    titles_text=[t.text for t in titles]
    print(titles_text)
    next=browser.find_element_by_css_selector('.next-button a')
    next.click()