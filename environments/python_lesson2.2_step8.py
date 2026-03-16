from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

#1. Открыть страницу http://suninjuly.github.io/file_input.html
browser = webdriver.Chrome()
browser.get(link)

#2. Заполнить текстовые поля: имя, фамилия, email
input_1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("name")
input_2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("lastname")
input_3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("test@test.ru")

#3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
directory = os.path.abspath(os.path.dirname(__file__))
file_name = "file_test.txt"
file_path = os.path.join(directory, file_name)
element = browser.find_element(By.ID, 'file').send_keys(file_path)

#4. Нажать кнопку "Submit"
submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(5)
browser.quit()