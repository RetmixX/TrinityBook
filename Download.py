from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import dataUser

class DownloadHTML:
    def __init__(self, logins):
        self.__logins = logins
        self.__url = "http://book.gta-trinity.ru/login?"

    def __createDriver(self):
        userAgent = UserAgent()
        settings = webdriver.ChromeOptions()
        settings.add_argument(f"user-agent={userAgent.chrome}")
        settings.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome("C:\\Users\\Retmix\\PycharmProjects\\parse\\chromedriver.exe", options=settings)
        return driver

    def __authorization(self):
        driver = self.__createDriver()
        driver.get(self.__url)
        driver.find_element(By.ID, "username").send_keys(dataUser.username)
        driver.find_element(By.ID, "password").send_keys(dataUser.password)
        driver.find_element(By.XPATH, "//*[@id=\"login\"]/div[5]/div[1]/button").click()
        return driver

    def downloadHTML(self):
        pathList = list()
        try:
            driver = self.__authorization()
            for nameUser in self.__logins:
                driver.get(f"http://book.gta-trinity.ru/{nameUser}")
                time.sleep(1)
                count = 100
                while not count == 0:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)
                    count -= 5
                with open(f"HtmlCode//{nameUser}_page.html", "w", encoding='utf-8') as file:
                    file.write(driver.page_source)
                    pathList.append(f"HtmlCode//{nameUser}_page.html")
            time.sleep(1)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
        return pathList


