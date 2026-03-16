from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

#Открыть страницу http://suninjuly.github.io/redirect_accept.html
browser = webdriver.Chrome()
browser.get(link)

#Нажать на кнопку
strange_button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()

#Переключиться на новую вкладку
new_windows = browser.window_handles[1]
browser.switch_to.window(new_windows)

#Пройти капчу для робота и получить число-ответ
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
y = calc(x_element)
input_answer = browser.find_element(By.ID, 'answer').send_keys(y)
button_answer = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()


time.sleep(5)
browser.quit()