#Открыть страницу http://suninjuly.github.io/file_input.html
#Заполнить текстовые поля: имя, фамилия, email
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit"

from selenium import webdriver
import time
import os

#Открыть страницу http://suninjuly.github.io/file_input.html.
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try: 

    #Заполнить текстовые поля: имя, фамилия, email
    first = browser.find_element_by_name("firstname")
    first.send_keys("ivan")
    
    first = browser.find_element_by_name("lastname")
    first.send_keys("ivanov")
	
    first = browser.find_element_by_name("email")
    first.send_keys("email")
	
    
	#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'hello.txt')           # добавляем к этому пути имя файла 
    
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
	
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