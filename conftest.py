import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def open_browsers(request):
    if request.param == 'chrome':
        chromeOptions = webdriver.ChromeOptions()
        #service_chrome = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())
        chromeOptions.add_experimental_option("prefs", {"download.default_directory": f"{os.getcwd()}\downloads"})
        chromeOptions.add_argument("--start-maximized")
        # chromeOptions.add_argument("--headless=new") #-- Без отображения окна браузера
        chrome_d = webdriver.Chrome(options=chromeOptions)
        driver = chrome_d
        request.cls.driver = driver
        driver.get('https://demoqa.com/')
        driver.implicitly_wait(10)
        print('\nОткрыт браузер Chrome')
        yield
        driver.quit()


    elif request.param == 'firefox':
        firefoxOptions = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        service_firefox = Service(executable_path=GeckoDriverManager().install())
        firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
        firefoxOptions.set_preference("browser.download.manager.showWhenStarting", False)
        firefoxOptions.set_preference("browser.download.folderList", 2)
        firefoxOptions.set_preference("browser.download.dir", f"{os.getcwd()}\downloads")
        # options.add_argument("--headless") #-- Без отображения окна браузера
        firefox_d = webdriver.Firefox(service=service_firefox, options=options)
        driver = firefox_d
        request.cls.driver = driver
        driver.get('https://demoqa.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        print('\nОткрыт браузер Firefox')
        yield
        driver.quit()