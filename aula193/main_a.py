from selenium import webdriver
from selenium.webdriver.common.by import By  # Para selecionar tags e seletores
from selenium.webdriver.common.keys import Keys
# Para aguardar a tela carregar o seletor.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


if __name__ == '__main__':
    TIME_TO_WAIT = 35
    browser = webdriver.Chrome()
    browser.get('https://www.google.com.br/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    # Escreveu no input
    search_input.send_keys('Hello world!')
    # Digitar enter.
    search_input.send_keys(Keys.ENTER)
    time.sleep(TIME_TO_WAIT)

    # Seleciona os resultados.
    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    # Encontra o primeiro link e clica nele.
    links[0].click()
    time.sleep(10)
