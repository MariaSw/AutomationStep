#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
import time
import math
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    authlink = "https://stepik.org/catalog?auth=login&language=ru"
    tasklink = "https://stepik.org/lesson/181384/step/8?unit=156009"
	
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)	
    
    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
	
    #assert "$100" in price
    #Нажать на кнопку "Book"
    button = browser.find_element_by_id("book")
    button.click()
	
	#Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text
	#Посчитать математическую функцию от x.
    y = calc(x)
	
	#Ввести ответ в текстовое поле.
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
	
	#Нажать на кнопку Submit.
    button1 = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "solve")))
    #browser.implicitly_wait(5)
    #button1 = browser.find_element_by_id("solve")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button1.click()
	
    #ответ отправить в степик
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    
    browser.get(authlink)
    browser.find_element_by_id('id_login_email').send_keys('kryvun_maria@mail.ru')# здесь вводится e-mail
    browser.find_element_by_id('id_login_password').send_keys('agriculture')# здесь вводится пароль
    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)
	
    browser.get(tasklink)
    browser.execute_script("window.scrollBy(0, 500);")
    answerstepik = browser.find_element_by_css_selector("div textarea")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answerstepik)
    answerstepik.send_keys(pyperclip.paste())
    
    #Нажать на кнопку Submit.
    #button2 = browser.find_element_by_css_selector("button.submit-submission")
    button2 = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()