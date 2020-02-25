#Открыть страницу http://SunInJuly.github.io/execute_script.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Открыть страницу http://SunInJuly.github.io/execute_script.html.
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try: 

    #Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text
	#Посчитать математическую функцию от x.
    y = calc(x)
	
	#Проскроллить страницу вниз.
	#Ввести ответ в текстовое поле.
    answer_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(y)

    #Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
	
    #Выбрать radiobutton "Robots rule!".
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    
	#Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла