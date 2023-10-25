import datetime
import os
import time
import allure
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from allure_commons.types import AttachmentType


class Methods():

    def __init__(self, driver):
        self.driver = driver


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

    """МЕТОД С ОЖИДАНИЕМ КЛИКАБЕЛЬНОСТИ С КЛИКОМ"""
    def element_to_be_clickable(self, locator):
        return wait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator)).click()

    """МЕТОД С ОЖИДАНИЕМ КЛИКАБЕЛЬНОСТИ БЕЗ КЛИКА"""
    def element_to_be_clickable_without_click(self, locator):
        return wait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator))

    """ОТОБРАЖЕНИЕ ЭЛЕМЕНТА"""
    def visibility_of_element_located(self, locator):
        return wait(self.driver, 20, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    """ОЖИДАНИЕ НАЛИЧИЯ ЭЛЕМЕНТА"""
    def presence_of_element_located(self, locator):
        return wait(self.driver, 20, poll_frequency=1).until(EC.presence_of_element_located(locator))

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
        variable_link = self.visibility_of_element_located(locator)
        with allure.step(f'Название ссылки {text_value}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Название ссылки {text_value}')
            assert variable_link.text == text_value
            print(f"Название ссылки: {variable_link.text} - УСПЕШНО")
            variable_link.click()
            Logger.add_end_step(method='Название ссылки')

    """КЛИК ПО КНОПКЕ"""
    def button_click(self, locator, button_text):
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Клик по кнопке {button_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Клик по кнопке, проверка названия кнопки {button_text}')
            assert variable_button.text == button_text
            print(f"Название кнопки: {variable_button.text} - УСПЕШНО")
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке, проверка названия кнопки')


    """БЕЗ КЛИКА ПО КНОПКЕ"""
    def button_without_click(self, locator, button_text):
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Без клика по кнопке {button_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Без клика по кнопке, проверка названия кнопки{button_text}')
            assert variable_button.text == button_text
            print(f"Название кнопки: {variable_button.text} - УСПЕШНО")
            Logger.add_end_step(method='Без клика по кнопке, проверка названия кнопки')


    """ДВОЙНОЙ КЛИК ПО КНОПКЕ"""
    def button_double_click(self, locator):
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Двойной клик по кнопке'):
            for i in range(2):
                variable_button.click()


    """КЛИК ПО КНОПКЕ БЕЗ ПРОВЕРКИ НАЗВАНИЯ"""
    def button_click_without_check_name(self, locator):
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')

    """КЛИК ПО РАДИО КНОПКЕ"""
    def radio_button_click(self, locator):
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')

    """КЛИК ПО ЧЕКБОКСУ"""
    def checkbox_click(self, locator, checkbox_text):
        variable_checkbox = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Клик по чекбоксу {checkbox_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Клик по чекбоксу {checkbox_text}')
            assert variable_checkbox.text == checkbox_text
            print(f"Название чекбокса: {variable_checkbox.text} - УСПЕШНО")
            variable_checkbox.click()
            Logger.add_end_step(method='Клик по чекбоксу')

    """КЛИК ПО ЧЕКБОКСУ БЕЗ ТЕКСТА"""
    def checkbox_click_without_text(self, locator):
        with allure.step('Клик по чекбоксу без текста'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по чекбоксу без текста')
            self.element_to_be_clickable(locator)
            Logger.add_end_step(method='Клик по чекбоксу без текста')

    """ЗАПОЛНЕНИЕ НЕОБЯЗАТЕЛЬНЫХ ПОЛЕЙ ВВОДА"""
    def field_optional_filling(self, locator_field, field_name, send_keys):
        with allure.step(f'Заполнение необязательных полей ввода {field_name}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Заполнение необязательных полей ввода {field_name}')
            name_field = self.element_to_be_clickable_without_click(locator_field)
            name_field.send_keys(Keys.CONTROL, 'a')
            name_field.send_keys(send_keys)

            assert name_field.get_attribute('value') == send_keys
            print(f"{field_name} {name_field.get_attribute('value')} - УСПЕШНО")
        Logger.add_end_step(method='Заполнение необязательных полей ввода')

    """ДОБАВЛЕНИЕ ИЗОБРАЖЕНИЯ"""
    def add_photo(self, locator_field, link):
        with allure.step(f'Добавление изображения {link}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Добавление изображения {link}')
            photo_add_button = self.element_to_be_clickable_without_click(locator_field)
            photo_add_button.send_keys(link)
            print("Изображение добавлено - УСПЕШНО")
            Logger.add_end_step(method='Добавление изображения')

    """ПРОВЕРКА ОТСУТСТВИЯ ЭЛЕМЕНТА"""
    def check_element_in_page_false(self, locator, element_name):
        with allure.step(f'Проверка отсутствия элемента: "{element_name}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Проверка отсутствия элемента: "{element_name}"')
            try:
                wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
                print(f'Элемент присутствует {element_name} - ОШИБКА!!!')
                text_print = 'False'
            except:
                print(f"Нет элемента {element_name} - УСПЕШНО")
                text_print = 'True'
            assert text_print == 'True'
            Logger.add_end_step(method='Проверка отсутствия элемента')

    """ПРОВЕРКА ПРИСУТСТВИЯ ЭЛЕМЕНТА"""
    def check_element_in_page_true(self, locator, element_name):
        with allure.step(f'Проверка присутствия элемента: "{element_name}"'):
            Logger.add_start_step(url=self.driver.current_url,
                                  method=f'Проверка присутствия элемента: "{element_name}"')
            try:
                wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
                print(f"Элемент отображается: {element_name} - УСПЕШНО")
                text_print = 'True'
            except:
                print(f'Элемент отсутствует: {element_name} - ОШИБКА!!!')
                text_print = 'False'
            assert text_print == 'True'
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
        date_now = datetime.datetime.now().strftime("%d.%m.%Y_время_%H.%M.%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Screenshot{date_now}", attachment_type=AttachmentType.PNG)
        screenshot_name = f'Снимок {date_now}.jpeg'
        self.driver.save_screenshot(f"{os.getcwd()}\\screenshots\{screenshot_name}")

    """ТЕКСТ НА СТРАНИЦАХ"""
    def text_on_pages(self, locator, text_name):
        name_text = self.visibility_of_element_located(locator)
        with allure.step(f'Текст на страницах: "{name_text.text}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Текст на страницах: "{text_name}"')
            assert name_text.text == text_name
            print(f"{name_text.text} - УСПЕШНО")
            Logger.add_end_step(method='Текст на страницах')

    """ВЫБОР ИЗ ВЫПАДАЮЩЕГО СПИСКА"""
    def list_dropdown_down_enter_choose(self, locator_field, locator_text):
        with allure.step(f'Выбор из выпадающего списка "{locator_text}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Выбор из выпадающего списка')
            self.element_to_be_clickable(locator_field)
            time.sleep(1)
            self.element_to_be_clickable(locator_text)
            print(f'Значение выбрано - УСПЕШНО')
            Logger.add_end_step(method='Выбор из выпадающего списка')