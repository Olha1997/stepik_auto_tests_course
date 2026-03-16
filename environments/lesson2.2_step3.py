from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

#1. Открыть страницу https://suninjuly.github.io/selects1.html
browser = webdriver.Chrome()
browser.get(link)

#2. Посчитать сумму заданных чисел
sum_numbers_str = str((int(browser.find_element(By.CSS_SELECTOR, 'h2>#num1').text)) + (int(browser.find_element(By.CSS_SELECTOR, 'h2>#num2').text)))

#3. Выбрать в выпадающем списке значение равное расчитанной сумме
dropdown = Select(browser.find_element(By.ID, 'dropdown')).select_by_visible_text(sum_numbers_str)

#4. Нажать кнопку "Submit"
button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

time.sleep(10)
browser.quit()
