import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 " 
              "Safari/537.36")

chrome_options = Options()
chrome_options.add_argument(f'user_agent={user_agent}')

# Инициализация веб-драйвера
driver = webdriver.Chrome(options=chrome_options)

try:
    # Открытие сайта
    driver.get("https://books.toscrape.com")

    pause_time = 2
    # Переход в раздел Travel
    travel_link = driver.find_element(By.XPATH, '//ul/li/ul/li[1]/a')
    time.sleep(pause_time)
    travel_link.click()

    # Выполнение скроллинга страницы вниз
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    time.sleep(pause_time)

    # Переход назад главную страницу
    travel_link = driver.find_element(By.XPATH, '//div[@class="col-sm-8 h1"]/a')
    travel_link.click()
    time.sleep(pause_time)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
