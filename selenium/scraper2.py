import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://www.cotodigital.com.ar/sitios/cdigi/categoria/csoyeatalogo-bebidas-bebidas-con-alcohol-vinos/_/N-uqiqtm"
driver.get(url)

# Esperar hasta que los productos se carguen
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "producto-card"))
# )

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# productos = soup.find_all("div", class_="producto-card")
# print("productos" )

# for producto in productos:
#     imagen = producto.find("img", class_="product-image")  # Buscar imagen dentro del producto
#     if imagen and imagen.has_attr("alt"):  # Verificar si la imagen tiene el atributo "alt"
#         nombre = imagen["alt"]
#         print(nombre.strip())  # Imprimir nombre del producto

# # Cerrar el navegador
# driver.quit()