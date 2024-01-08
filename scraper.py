import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import mailer

chrome_path = ""
productos = ["AMD Ryzen 5 5600X 3.7GHz", "AMD Ryzen 7 5800X 3.8GHz"]


class stockChecker:
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://www.augustushotels.es/")
        sleep(3)
        

    def _find_product(self, product):
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/form/div[1]/img").click()
        sleep(3)
        search_box = self.driver.find_element_by_xpath("/html/body/header/div[3]/div[1]/div/div[2]/div/form/input")
        search_box.send_keys(product)
        self.driver.find_element_by_xpath("/html/body/header/div[3]/div[2]/section/div[2]/div[2]/ol/li[1]/a").click()

    def get_availability(self, product):
        self._find_product(product)
        try:
            boton_avisame = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div[4]/div[3]/div/div/div/button[3]/strong").text
            precio = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[1]").text
            estado_precio = product + " no disponible, precio:" + precio
            return estado_precio
        except selenium.common.exceptions.NoSuchElementException:
            precio = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[1]").text
            estado_precio = product + " no disponible, precio: " + precio
            return estado_precio

    def get_motherboard_prices(self,chipset):
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/nav/div[1]/h3").click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/nav/div[3]/ul/li[2]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/ul/li[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div[4]/div/a").click()

    def close_win(self):
        self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[1]/div[1]/div/form/div[1]/img').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/aside/div/div/div[2]/button[1]').click()
        #self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/form/div[1]/img").click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/button').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/input').send_keys('05/08/2024')
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[1]/div/div[3]/div/div/div/button').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[1]/div/div[3]/div/div/div/input').send_keys('19/08/2024')
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[1]/div/div[4]/button[1]').click()
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[1]/div/div[4]/button[1]').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[2]/div/input[2]').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[2]/div/input[2]').send_keys('cortidecor46@hotmail.com')
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div/div/div/div[2]/div/div/form/div[2]/div/button').click()
        sleep(10)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/form/button').click()
        sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[4]/table/tbody/tr[4]/td[3]').text
        sleep(50)



finder = stockChecker(chrome_path)
precio = finder.close_win()
mailer.main(precio)