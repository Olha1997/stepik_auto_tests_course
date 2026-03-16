from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

#1. Открыть страницу http://suninjuly.github.io/alert_accept.html
browser = webdriver.Chrome()
browser.get(link)

#2. Нажать на кнопку
first_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

#3. Принять confirm
confirm = browser.switch_to.alert.accept()

#4. На новой странице решить капчу для роботов, чтобы получить число с ответом
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
y = calc(x_element)
input_answer = browser.find_element(By.ID, 'answer').send_keys(y)
button_answer = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(5)
browser.quit()