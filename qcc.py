from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver1 = webdriver.Chrome()
driver1.get('https://www.qcc.com/')
driver1.maximize_window()
# driver1.implicitly_wait(5)

search = driver1.find_element_by_id('searchkey')
print(search)
# btn = WebDriverWait(driver1, 10, 1).until(lambda x: x.find_element_by_xpath('//*[@id="indexSearchForm"]/div[1]/span/input'))
btn1 = driver1.find_element_by_xpath('//*[@id="indexSearchForm"]/div[1]/span/input')
print(btn1)
search.send_keys('汉科软')
btn1.click()

# 第一个结果
sleep(5)
print(driver1.title)
tar = driver1.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/table/tr[1]/td[3]/div/a[1]')
tar.click()

sleep(4)
driver1.quit()
getattr()



