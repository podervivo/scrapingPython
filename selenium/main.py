from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

USSER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    #config del browser
    service = Service(ChromeDriverManager().install())
    option = Options()
    #option.add_argument('--headless')
    option.add_argument('--window-size=1920,1080')
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
   #login 
    user_input = driver.find_element(By.ID, "user-name").send_keys(USSER)
    user_pass = driver.find_element(By.ID, "password").send_keys(PASSWORD)
    time.sleep(2)
    login_button = driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    #compras
    driver.find_element(By.NAME,"add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)
    #carrito
    driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()
    time.sleep(2)
    #checkout
    driver.find_element(By.ID,"checkout").click()
    time.sleep(2)
    #payment
    driver.find_element(By.ID, "first-name").send_keys("test")
    driver.find_element(By.ID, "last-name").send_keys("passtest")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    time.sleep(2)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "finish").click()
    #volver a los productos
    driver.find_element(By.ID, "back-to-products").click()

    time.sleep(10)
    
   




    time.sleep(10)
    driver.quit()
    
if __name__ == '__main__':
    main()