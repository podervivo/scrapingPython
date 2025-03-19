import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.ar/_Container_mk-t2-cyberfest-2025-fashion-zapatillas#deal_print_id=4ffd5c80-00cf-11f0-bc53-c53395f3b1c6&c_id=special-withoutlabel&c_element_order=6&c_campaign=ZAPATILLAS&c_uid=4ffd5c80-00cf-11f0-bc53-c53395f3b1c6"
response = requests.get(url)

if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        productos = soup.find_all("div", class_="andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated")
        #print(productos)
        for producto in productos:
            
            titulo = producto.find("h3", class_="poly-component__title-wrapper")
            if titulo:
                print(titulo.text.strip())
else:
    print("falla")