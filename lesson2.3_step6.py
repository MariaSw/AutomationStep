#Открыть страницу http://suninjuly.github.io/redirect_accept.html
#Нажать на кнопку
#Переключиться на новую вкладку
#Пройти капчу для робота и получить число-ответ

from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    link2 = "https://stepik.org/lesson/184253/step/4?unit=158843"
	
    #Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser = webdriver.Chrome()
    browser.get(link)
	
	#Нажать на кнопку
    trollbut = browser.find_element_by_css_selector("button.trollface")
    time.sleep(5)
    trollbut.click()
	
    #Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
	
	#Пройти капчу для робота и получить число-ответ
	#Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text
	#Посчитать математическую функцию от x.
    y = calc(x)
	
	#Ввести ответ в текстовое поле.
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
	
	#Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
	