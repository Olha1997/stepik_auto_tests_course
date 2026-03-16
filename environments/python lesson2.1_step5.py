from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

#Открыть страницу https://suninjuly.github.io/math.html
browser = webdriver.Chrome()
browser.get(link)

#Считать значение для переменной x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#Посчитать математическую функцию от x
x_element = browser.find_element(By.CSS_SELECTOR, '[class="form-group"] label .nowrap:nth-child(2)').text
y = calc(x_element)

#Ввести ответ в текстовое поле
input_for_answers = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

#Отметить checkbox "I'm the robot".
checkbox_robot = browser.find_element(By.ID, "robotCheckbox").click()

#Выбрать radiobutton "Robots rule!".
radiobutton_robots_rule = browser.find_element(By.ID, "robotsRule").click()

#Нажать на кнопку Submit.
button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

time.sleep(10)
browser.quit()

