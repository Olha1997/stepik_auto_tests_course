import time

from selenium import webdriver
from selenium.webdriver.common.by import By #импорт модуля
link = "http://suninjuly.github.io/simple_form_find_task.html" #задали значение link
try: #указали что сделать
    browser = webdriver.Chrome() #открыть браузер
    browser.get(link) #перейти по заданной ссылке
    button = browser.find_element(By.ID, "submit_button") #найти кнопку
    button.click() #нажать на кнопку
    time.sleep(5)
finally: #указали, что сделать напоследок
    browser.quit() #закрыли браузер