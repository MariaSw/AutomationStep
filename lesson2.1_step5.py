#Открыть страницу http://suninjuly.github.io/math.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку Submit.


from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    #Открыть страницу http://suninjuly.github.io/math.html.
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	#Считать значение для переменной x.
	#Посчитать математическую функцию от x (код для этого приведён ниже).
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

	#Ввести ответ в текстовое поле.
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
	
	#Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
	
    #Выбрать radiobutton "Robots rule!".
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    
	#Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# альтернативно
    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').click()