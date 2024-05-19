# bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# garantia de ter o ultima versao webdriver manager instalado
servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)

busca = "letra de planet hemp mantenha o respeito"

# buscando pagina do correio no google chrome
site = "https://www.google.com.br"
browser.get(site)
# tempo de espera para garantia de tudo carregar
time.sleep(3)
# clicando na barra de busca e buscando a musica
browser.find_element(By.ID, 'APjFqb').send_keys(busca)
# tempo de espera para garantia de tudo carregar
time.sleep(3)
# buscando a letra da musica
browser.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
# tempo de espera para garantia de tudo carregar
time.sleep(3)
# localizando a div da leta
div_element = browser.find_element(By.CSS_SELECTOR, 'div[jsname="WbKHeb"]')
# extraindo o texto da div
div_text = div_element.text
# encerrando instancia browser
browser.quit()
# mostrando resultado no terminal
letra_completa = div_text
print(letra_completa)
