
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Users\\Мадияр\\Desktop\\Test\\chromedriver.exe')

#from selenium import webdriver

driver.get("https://github.com/login")
# найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
driver.find_element_by_id("login_field").send_keys('Madiyar-data')
# найти поле ввода пароля и также вставить пароль
driver.find_element_by_id("password").send_keys('Parol2$2')
# нажмите кнопку входа в систему
driver.find_element_by_name("commit").click()


