from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver1 = webdriver.Chrome()
driver1.get('https://www.zhihu.com/')
driver1.maximize_window()


driver1.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]').click()
driver1.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[2]/div/label/input').send_keys('17613712051')
driver1.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys('15326334205205qz')
driver1.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button').click()
# 请求失败

sleep(5)
driver1.quit()


