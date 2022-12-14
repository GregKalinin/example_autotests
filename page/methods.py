import datetime
import os
import time
import openpyxl
from openpyxl import load_workbook
import allure
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from utilities.logger import Logger


class Methods():

    def __init__(self, driver):
        self.driver = driver

    def browser_open(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\\git_hub\\example_autotests\\downloads"})
        chrome_d = webdriver.Chrome(executable_path="C:\\git_hub\\example_autotests\\driver\\chromedriver.exe", options=chromeOptions)
        self.driver = chrome_d
        self.driver.get('https://demoqa.com/')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def browser_open_firefox(self):
        firefoxOptions = webdriver.FirefoxProfile()
        firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
        firefoxOptions.set_preference("browser.download.manager.showWhenStarting", False)
        firefoxOptions.set_preference("browser.download.dir",
                                      "C:\\git_hub\\example_autotests\\downloads")
        firefox_d = webdriver.Firefox(
            executable_path="C:\\git_hub\\example_autotests\\driver\\geckodriver.exe",
            firefox_profile=firefoxOptions)
        self.driver = firefox_d
        self.driver.get('https://demoqa.com/')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    """ПОЛУЧЕНИЕ ТЕКУЩЕГО URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Текущий URL:', + get_url)


    """АВТОРИЗАЦИЯ"""
    def authorization(self, login_field, password_field, locator_login, locator_pass, locator_button):
        with allure.step('Авторизация'):
            Logger.add_start_step(url=self.driver.current_url, method='Авторизация')
            # ввод логина
            login = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_login))
            login.send_keys(login_field)

            # ввод пароля
            password = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_pass))
            password.send_keys(password_field)

            # Кнопка "Войти(страница логина)"
            enter_button = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_button)).click()
            Logger.add_end_step(method='Авторизация')

    """ОЖИДАНИЕ КЛИКАБЕЛЬНОСТИ"""
    def element_to_be_clickable(self, locator):
        return wait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    """ОТОБРАЖЕНИЕ ЭЛЕМЕНТА"""
    def visibility_of_element_located(self, locator):
        return wait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    """СКРОЛЛИНГ СТРАНИЦЫ ВНИЗ"""
    def scrolling_page_down(self):
        with allure.step('Прокрутка вниз'):
            self.driver.execute_script("window.scrollBy(0, 600);")

    def scrolling_page_down_300(self):
        with allure.step('Прокрутка вниз'):
            self.driver.execute_script("window.scrollBy(0, 300);")

    """СКРОЛЛИНГ СТРАНИЦЫ ВВЕРХ"""
    def scrolling_page_up(self):
        with allure.step('Прокрутка вверх'):
            self.driver.execute_script("window.scrollBy(0, -600);")

    def scrolling_page_up_300(self):
        with allure.step('Прокрутка вверх'):
            self.driver.execute_script("window.scrollBy(0, -300);")

    """НАЗВАНИЕ ССЫЛКИ И КЛИК"""
    def check_link_click(self, locator, text_value):
        with allure.step('Название ссылки'):
            Logger.add_start_step(url=self.driver.current_url, method='Название ссылки')
            variable_link = wait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            assert variable_link.text == text_value
            print(f"Название ссылки: {variable_link.text} - УСПЕШНО")
            variable_link.click()
            Logger.add_end_step(method='Название ссылки')

    """КЛИК ПО КНОПКЕ"""
    def button_click(self, locator, button_text):
        with allure.step('Клик по кнопке'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке, проверка названия кнопки')
            variable_button = wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            assert variable_button.text == button_text
            print(f"Название кнопки: {variable_button.text} - УСПЕШНО")
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке, проверка названия кнопки')


    """БЕЗ КЛИКА ПО КНОПКЕ"""
    def button_without_click(self, locator, button_text):
        with allure.step('Без клика по кнопке'):
            Logger.add_start_step(url=self.driver.current_url, method='Без клика по кнопке, проверка названия кнопки')
            variable_button = wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            assert variable_button.text == button_text
            print(f"Название кнопки: {variable_button.text} - УСПЕШНО")
            Logger.add_end_step(method='Без клика по кнопке, проверка названия кнопки')


    """ДВОЙНОЙ КЛИК ПО КНОПКЕ"""
    def button_double_click(self, locator):
        with allure.step('Двойной клик по кнопке'):
            variable_button = wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            for i in range(2):
                variable_button.click()


    """КЛИК ПО КНОПКЕ БЕЗ ПРОВЕРКИ НАЗВАНИЯ"""
    def button_click_without_check_name(self, locator):
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button = wait(self.driver, 20).until(EC.element_to_be_clickable(locator))
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')

    """КЛИК ПО РАДИО КНОПКЕ"""
    def radio_button_click(self, locator):
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button = wait(self.driver, 20).until(EC.element_to_be_clickable(locator))
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')

    """КЛИК ПО ЧЕКБОКСУ"""
    def checkbox_click(self, locator, checkbox_text):
        with allure.step('Клик по чекбоксу'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по чекбоксу')
            variable_checkbox = wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            assert variable_checkbox.text == checkbox_text
            print(f"Название чекбокса: {variable_checkbox.text} - УСПЕШНО")
            variable_checkbox.click()
            Logger.add_end_step(method='Клик по чекбоксу')

    """КЛИК ПО ЧЕКБОКСУ БЕЗ ТЕКСТА"""
    def checkbox_click_without_text(self, locator):
        with allure.step('Клик по чекбоксу без текста'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по чекбоксу без текста')
            variable_checkbox = wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            variable_checkbox.click()
            Logger.add_end_step(method='Клик по чекбоксу без текста')

    """ЗАПОЛНЕНИЕ НЕОБЯЗАТЕЛЬНЫХ ПОЛЕЙ ВВОДА"""
    def field_optional_filling(self, locator_field, field_name, send_keys):
        with allure.step('Заполнение необязательных полей ввода'):
            Logger.add_start_step(url=self.driver.current_url, method='Заполнение необязательных полей ввода')
            name_field = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_field))
            name_field.send_keys(Keys.CONTROL, 'a')
            name_field.send_keys(send_keys)

            assert name_field.get_attribute('value') == send_keys
            print(f"{field_name} {name_field.get_attribute('value')} - УСПЕШНО")
        Logger.add_end_step(method='Заполнение необязательных полей ввода')

    """ДОБАВЛЕНИЕ ИЗОБРАЖЕНИЯ"""
    def add_photo(self, locator_field, link):
        with allure.step('Добавление изображения'):
            Logger.add_start_step(url=self.driver.current_url, method='Добавление изображения')
            photo_add_button = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_field))
            photo_add_button.send_keys(link)
            print("Изображение добавлено - УСПЕШНО")
            Logger.add_end_step(method='Добавление изображения')

    """ПРОВЕРКА ОТСУТСТВИЯ ЭЛЕМЕНТА"""
    def check_element_in_page_false(self, locator):
        with allure.step('Проверка отсутствия элемента'):
            Logger.add_start_step(url=self.driver.current_url, method='Проверка отсутствия элемента')
            try:
                variable_button = wait(self.driver, 2).until(EC.element_to_be_clickable(locator))
            except:
                print("Нет элемента - УСПЕШНО")
            Logger.add_end_step(method='Проверка отсутствия элемента')

    """ПРОВЕРКА ПРИСУТСТВИЯ ЭЛЕМЕНТА"""
    def check_element_in_page_true(self, locator):
        with allure.step('Проверка присутствия элемента'):
            Logger.add_start_step(url=self.driver.current_url, method='Проверка присутствия элемента')
            variable_button = wait(self.driver, 2).until(EC.element_to_be_clickable(locator))
            if TimeoutException:
                print("Элемент отображается - УСПЕШНО")
            else:
                print('Элемент отсутствует - ОШИБКА!!!!!!!!!!!!!!')
            Logger.add_end_step(method='Проверка присутствия элемента')

    """ПЕРЕКЛЮЧЕНИЕ НА МОДАЛЬНОЕ ОКНО С СООБЩЕНИЕМ"""
    def is_alert_present(self):
        with allure.step('Переключение на модальное окно с сообщением'):
            try:
                self.driver.switch_to_alert()
            except NoAlertPresentException:
                return False

    """СКРИНШОТ"""
    def get_screenshot(self):
        date_now = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = 'Снимок' + date_now + '.jpeg'
        self.driver.save_screenshot("C:\\git_hub\\example_autotests\\screenshots\\" + screenshot_name)

    """ТЕКСТ НА СТРАНИЦАХ"""
    def text_on_pages(self, locator, text_name):
        with allure.step('Текст на страницах'):
            Logger.add_start_step(url=self.driver.current_url, method='Текст на страницах')
            step_name_text = wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            assert step_name_text.text == text_name
            print(f"{step_name_text.text} - УСПЕШНО")
            Logger.add_end_step(method='Текст на страницах')

    """ВЫБОР ИЗ ВЫПАДАЮЩЕГО СПИСКА"""
    def list_dropdown_down_enter_choose(self, locator_field, locator_text):
        with allure.step('Выбор из выпадающего списка'):
            Logger.add_start_step(url=self.driver.current_url, method='Выбор из выпадающего списка')
            name_field = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_field)).click()
            time.sleep(1)
            name_field = wait(self.driver, 10).until(EC.element_to_be_clickable(locator_text)).click()
            print('Значение выбрано - УСПЕШНО')
            Logger.add_end_step(method='Выбор из выпадающего списка')