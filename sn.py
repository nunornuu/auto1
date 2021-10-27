from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver1 = webdriver.Chrome()
driver1.get('https://www.suning.com/')
driver1.maximize_window()

driver1.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()
driver1.find_element_by_id('userName').send_keys('17613712051')
driver1.find_element_by_id('password').send_keys('15326334205205qz')
# 滑动验证,短信验证
driver1.find_element_by_xpath('//*[@id="submit"]').click()



driver1.quit()




