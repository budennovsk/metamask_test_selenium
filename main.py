import time
from secret_key import secret_fraz, password_me, NETWORK

import selenium_metamask_automation

# запускаем расширения библиотеки селениум
selenium_metamask_automation.downloadMetamaskExtension()


def connect_METAMASK():
    """ Авторизуемся в метамаск кошелеке и регистрируемся на сайте аирдроп """
    # путь до драйвера
    driver = selenium_metamask_automation.launchSeleniumWebdriver(r'E:\Django\first\chromedriver\chromedriver.exe')
    # переключаем на главный экран
    driver.switch_to.window(driver.window_handles[0])
    # подключаемся к сайту на котором будет автоматизация
    driver.get("https://portfolio.metamask.io/")

    # вызываем функцию, которой передаем секретную фразу и пароль от кошелька
    selenium_metamask_automation.metamaskSetup(secret_fraz, password_me)
    # изменяем тестовую сеть после авторизации кошелька
    selenium_metamask_automation.changeMetamaskNetwork(NETWORK)
    # переходим на сайт для соединения кошельков
    driver.get("https://app.airdrop-hunter.site/")
    time.sleep(3)
    # выбираем МЕТУ
    driver.find_element_by_xpath('//*[@id="WEB3_CONNECT_MODAL_ID"]/div/div/div[2]/div[1]/div').click()
    time.sleep(3)
    # переключаемся между окнами браузера
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    # выбираем кнопку "Отмена"
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div/div/div[3]/div/div[3]/button').click()
    time.sleep(3)
    # выбираем кнопку "Далее"
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[2]/div[2]/footer/button[1]').click()
    time.sleep(3)
    # выбираем кнопку "Далее"
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    time.sleep(3)
    # выбираем кнопку "Подключить"
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    time.sleep(3)
    # переходим на главное меню сайта для проверки подключения кошелька
    driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
    connect_METAMASK()
