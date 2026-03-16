from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

#1. Открыть страницу http://suninjuly.github.io/get_attribute.html
browser = webdriver.Chrome()
browser.get(link)

#2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами
treasure_chest = browser.find_element(By.ID, "treasure")

#3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
x_for_treasure_chest = treasure_chest.get_attribute("valuex")

#4. Посчитать математическую функцию от x (сама функция остаётся неизменной)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
y = calc(x_for_treasure_chest)
print(y)

#5. Ввести ответ в текстовое поле
input_for_answers = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

#6. Отметить checkbox "I'm the robot".
checkbox_robot = browser.find_element(By.ID, "robotCheckbox").click()

#7. Выбрать radiobutton "Robots rule!".
radiobutton_robots_rule = browser.find_element(By.ID, "robotsRule").click()

#8. Нажать на кнопку Submit.
button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

time.sleep(10)
browser.quit()

