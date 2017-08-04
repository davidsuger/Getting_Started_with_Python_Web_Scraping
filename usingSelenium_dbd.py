from selenium import webdriver

# browser = webdriver.Chrome("chromedriver.exe")
browser = webdriver.Firefox()

browser.get('http://dbd.jd.com/listing/0-93-7000-0-111-0-0-1-0-0.html')
# for i in range(2):
#     titles=browser.find_elements_by_css_selector('.name>a')
#     titles_text=[t.text for t in titles]
#     print(titles_text)
#     next=browser.find_element_by_css_selector('.pn-next')
#     next.click()

next=browser.find_element_by_css_selector('.pn-next')