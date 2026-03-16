from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/execute_script.html'

#1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
browser = webdriver.Chrome()
browser.get(link)

#2.Считать значение для переменной x.
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#3.Посчитать математическую функцию от x.
x_element = browser.find_element(By.CSS_SELECTOR, 'label>.nowrap:nth-child(2)').text
y = calc(x_element)

#4. Проскроллить страницу вниз.
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("window.scrollBy(0, 100);", button)
time.sleep(1)

#5. Ввести ответ в текстовое поле.
input_answer = browser.find_element(By.ID, 'answer').send_keys(y)

#6. Выбрать checkbox "I'm the robot".
robot_box = browser.find_element(By.ID, 'robotCheckbox').click()

#7. Переключить radiobutton "Robots rule!".
robot_radiobutton = browser.find_element(By.ID, "robotsRule").click()

#8. Нажать на кнопку "Submit".
button_submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

time.sleep(5)
browser.quit()

