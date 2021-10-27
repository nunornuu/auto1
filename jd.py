from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver1 = webdriver.Chrome()
driver1.get('https://www.jd.com/')
driver1.maximize_window()
driver1.implicitly_wait(15)

act = ActionChains(driver1)
login_btn = driver1.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]')
act.move_to_element(login_btn)
sleep(1)
act.click().perform()
# login_btn.click()
driver1.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
driver1.find_element_by_id('loginname').send_keys('17613712051')
driver1.find_element_by_id('nloginpwd').send_keys('15326334205205qz')
driver1.find_element_by_id('loginsubmit').click()

# 拼图
# scroll_btn = driver1.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
# act.click_and_hold(scroll_btn)
# try:
#     for i in range(2, 253, 2):
#         act.move_by_offset(i, 0)
#         sleep(1)
# except Exception:
#     pass
# act.move_by_offset(100, 0)

# act.perform()

sleep(5)
# 点击短信验证
try:
    driver1.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/button').click()
except Exception:
    print('hh')
finally:
    sleep(5)
    driver1.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/button').click()
driver1.quit()







