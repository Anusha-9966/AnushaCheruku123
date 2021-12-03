
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')

driver.maximize_window()
driver.get("http://www.google.com")
print(driver.title)

#driver.find_element_by_name("q").send_keys("citrine online exams")
#driver.find_element_by_name("q").send_keys(Keys.ENTER)
#driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div[1]/a/h3").click()

driver.get("http://192.168.1.52:8094/login/")
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='header']/div/a").click()   #login
driver.find_element_by_xpath("//a[@id='register-tab']").click()   #register
time.sleep(2)

driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Shanvitha")
print('Shanvitha')
time.sleep(1)

driver.find_element_by_xpath("//input[@id='mobile']").send_keys("9966484650")
driver.find_element_by_xpath("//input[@id='ms-form-email-r']").send_keys("anushareddy462@gmail.com")

select_course = driver.find_element_by_xpath("//select[@id='selec_course']")
time.sleep(1)
drp= Select(select_course)
drp.select_by_index(1)

select_class = driver.find_element_by_xpath("//select[@id='select_class']")
time.sleep(1)
drp= Select(select_class)
drp.select_by_index(7)

driver.find_element_by_xpath("//*[@id='submit_reg']").click()
time.sleep(2)
a = Alert(driver)
print(a.text)
a .accept()



driver.find_element_by_xpath("//*[@id='logintb']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ms-form-user']").send_keys("anushareddy462@gmail.com")
driver.find_element_by_xpath("//*[@id='ms-form-pass']").send_keys("1111122")
driver.find_element_by_xpath("//*[@id='UserCaptchaCode']").click()

time.sleep(4)
driver.quit()