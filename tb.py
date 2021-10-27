from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver1 = webdriver.Chrome()
driver1.get('https://www.taobao.com/')
driver1.maximize_window()
# driver1.implicitly_wait(15)

act = ActionChains(driver1)
login_btn = driver1.find_element_by_xpath('//*[@id="J_SiteNavMytaobao"]/div[1]/a')
act.move_to_element(login_btn)
sleep(1)
act.click()
act.perform()

driver1.find_element_by_id('fm-login-id').send_keys('123123')
driver1.find_element_by_id('fm-login-password').send_keys('213123')
driver1.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
# 滑动失效

sleep(4)
driver1.quit()


