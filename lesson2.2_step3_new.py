#Открыть страницу http://suninjuly.github.io/selects1.html
#Посчитать сумму заданных чисел
#Выбрать в выпадающем списке значение равное расчитанной сумме
#Нажать кнопку "Submit"

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

#Открыть страницу http://suninjuly.github.io/selects1.html
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try: 
	
	#Посчитать сумму заданных чисел
    slag1 = int(browser.find_element_by_id("num1").text)
    slag2 = int(browser.find_element_by_id("num2").text)
    
    listA = [
    slag1,
    slag2
    ]
    sumstr = str(sum(listA))
	
	#Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sumstr) 
	
	#Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()