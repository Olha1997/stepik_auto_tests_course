from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
browser = webdriver.Chrome()
browser.get(link)

try:

    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    #Нажать на кнопку "Book"
    button_book = browser.find_element(By.ID, 'book').click()

    #Проскроллили вниз до кнопки
    browser.execute_script("window.scrollBy(0, 100);", button_book)
    time.sleep(1)

    #Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x_element)
    input_answer = browser.find_element(By.ID, 'answer').send_keys(y)
    click_button = browser.find_element(By.ID, "solve").click()

finally:
    browser.quit()