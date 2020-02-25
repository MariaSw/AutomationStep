#Открыть страницу http://suninjuly.github.io/alert_accept.html
#Нажать на кнопку
#Принять confirm
#На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Открыть страницу http://suninjuly.github.io/alert_accept.html.


try:

    link = "http://suninjuly.github.io/alert_accept.html"
    authlink = "https://stepik.org/catalog?auth=login&language=ru"
    tasklink = "https://stepik.org/lesson/184253/step/4?thread=solutions&unit=158843"
	
	
    browser = webdriver.Chrome()
    browser.get(link) 

    #Нажать на кнопку
    journey = browser.find_element_by_css_selector("button.btn-primary")
    journey.click()
	
	#Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

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
	
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    
    browser.get(authlink)
    time.sleep(5)
    browser.find_element_by_id('id_login_email').send_keys('kryvun_maria@mail.ru')# здесь вводится e-mail
    browser.find_element_by_id('id_login_password').send_keys('agriculture')# здесь вводится пароль
    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)
	
    browser.get(tasklink)
    time.sleep(3)
    browser.execute_script("window.scrollBy(0, 500);")
    answerstepik = browser.find_element_by_css_selector("div textarea")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answerstepik)
    answerstepik.send_keys(pyperclip.paste())
    
    #Нажать на кнопку Submit.
    button2 = browser.find_element_by_css_selector("button.submit-submission")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
   
	
	