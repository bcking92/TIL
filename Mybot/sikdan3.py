from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
url = 'http://edu.ssafy.com/edu/board/notice/list.do'

month = '07'
week = '4'
# driver.find_element_by_xpath(f'//a[contains(@text,"{month}월 {week}주차"]').click()
driver.get(url)