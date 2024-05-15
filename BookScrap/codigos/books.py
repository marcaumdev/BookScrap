"""
Nós queremos acessar a pagina, pegar todos os links dos livros,
acessar cada link em busca da quantidade de livros em estoque
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/"
driver.get(url)
time.sleep(2)

elementosTitulo = driver.find_elements(By.TAG_NAME, 'a')[54:92:2]
listaTitulos = [title.get_attribute("title") for title in elementosTitulo]

listaStok = []
for titulo in elementosTitulo:
    titulo.click()
    time.sleep(1)
    stok = driver.find_element(By.CLASS_NAME, 'instock').text
    qtd = int(stok.replace("In stock (", '').replace(" available)", ""))
    listaStok.append(qtd)
    driver.back()
    time.sleep(1)

x = 0
data = {"Titulo": listaTitulos, "Estoque": listaStok}
dados = pd.DataFrame(data)
dados.to_excel("dados.xlsx")