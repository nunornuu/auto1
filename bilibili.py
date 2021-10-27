from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


driver1 = webdriver.Chrome()
driver1.get('https://www.bilibili.com/')
driver1.maximize_window()
# driver1.implicitly_wait(15)


try:
    rt = driver1.find_element_by_xpath('//*[@id="i_cecream"]/div[2]/div/div/button[1]')
except NoSuchElementException:
    pass
else:
    rt.click()

# print(rt)
sleep(4)
login_btn = driver1.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div')

act = ActionChains(driver1)
act.move_to_element(login_btn)
sleep(2)
act.click()
act.perform()
driver1.switch_to.window(driver1.window_handles[1])


driver1.find_element_by_id('login-username').send_keys('17613712051')
driver1.find_element_by_id('login-passwd').send_keys('15326334205205qz')
driver1.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()

sleep(8)
try:
    driver1.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a/div').click()
except NoSuchElementException:
    pass
sleep(5)
driver1.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys('鬼畜')
driver1.find_element_by_xpath('//*[@id="nav_searchform"]/div').click()

sleep(6)
driver1.switch_to.window(driver1.window_handles[2])
driver1.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/a/div/div[1]/img').click()
sleep(5)
driver1.quit()

