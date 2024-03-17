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
        self.wait = wait(self.driver, 10, poll_frequency=1)

    def element_to_be_clickable(self, locator):
        """МЕТОД С ОЖИДАНИЕМ КЛИКАБЕЛЬНОСТИ С КЛИКОМ"""
        return wait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator)).click()

    def element_to_be_clickable_without_click(self, locator):
        """МЕТОД С ОЖИДАНИЕМ КЛИКАБЕЛЬНОСТИ БЕЗ КЛИКА"""
        return wait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator))

    def visibility_of_element_located(self, locator):
        """ОТОБРАЖЕНИЕ ЭЛЕМЕНТА"""
        return wait(self.driver, 20, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def presence_of_element_located(self, locator):
        """ОЖИДАНИЕ НАЛИЧИЯ ЭЛЕМЕНТА"""
        return wait(self.driver, 20, poll_frequency=1).until(EC.presence_of_element_located(locator))


    def get_current_url(self):
        """ПОЛУЧЕНИЕ ТЕКУЩЕГО URL"""
        get_url = self.driver.current_url
        print('Текущий URL:', + get_url)


    def authorization(self, login_field, password_field, locator_login, locator_pass, locator_button):
        """АВТОРИЗАЦИЯ"""
        with allure.step('Авторизация'):
            Logger.add_start_step(url=self.driver.current_url, method='Авторизация')
            # ввод логина
            self.element_to_be_clickable_without_click(locator_login).send_keys(login_field)

            # ввод пароля
            self.element_to_be_clickable_without_click(locator_pass).send_keys(password_field)

            # Кнопка "Войти(страница логина)"
            self.element_to_be_clickable(locator_button)
            Logger.add_end_step(method='Авторизация')


    def scrolling_page(self, x=0, y=0):
        """ПРОКРУТКА СТРАНИЦЫ"""
        with allure.step('Прокрутка страницы'):
            self.driver.execute_script(f"window.scrollBy({x}, {y})")


    def check_link_click(self, locator, text_value):
        """НАЗВАНИЕ ССЫЛКИ И КЛИК"""
        variable_link = self.visibility_of_element_located(locator)
        with allure.step(f'Название ссылки {text_value}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Название ссылки {text_value}')
            assert variable_link.text == text_value
            print(f"Название ссылки: {variable_link.text} - УСПЕШНО")
            variable_link.click()
            Logger.add_end_step(method='Название ссылки')


    def button_click(self, locator, button_text):
        """КЛИК ПО КНОПКЕ"""
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Клик по кнопке {button_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Клик по кнопке, проверка названия кнопки {button_text}')
            assert variable_button.text == button_text
            print(f"Название кнопки: {variable_button.text} - УСПЕШНО")
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке, проверка названия кнопки')


    def button_without_click(self, locator, button_text):
        """БЕЗ КЛИКА ПО КНОПКЕ"""
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Без клика по кнопке {button_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Без клика по кнопке, проверка названия кнопки{button_text}')
            assert variable_button.text == button_text
            print(f"Название кнопки: {variable_button.text} - УСПЕШНО")
            Logger.add_end_step(method='Без клика по кнопке, проверка названия кнопки')


    def button_double_click(self, locator):
        """ДВОЙНОЙ КЛИК ПО КНОПКЕ"""
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Двойной клик по кнопке'):
            for i in range(2):
                variable_button.click()


    def button_click_without_check_name(self, locator):
        """КЛИК ПО КНОПКЕ БЕЗ ПРОВЕРКИ НАЗВАНИЯ"""
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')


    def radio_button_click(self, locator):
        """КЛИК ПО РАДИО КНОПКЕ"""
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')


    def checkbox_click(self, locator, checkbox_text):
        """КЛИК ПО ЧЕКБОКСУ"""
        variable_checkbox = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Клик по чекбоксу {checkbox_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Клик по чекбоксу {checkbox_text}')
            assert variable_checkbox.text == checkbox_text
            print(f"Название чекбокса: {variable_checkbox.text} - УСПЕШНО")
            variable_checkbox.click()
            Logger.add_end_step(method='Клик по чекбоксу')


    def checkbox_click_without_text(self, locator):
        """КЛИК ПО ЧЕКБОКСУ БЕЗ ТЕКСТА"""
        with allure.step('Клик по чекбоксу без текста'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по чекбоксу без текста')
            self.element_to_be_clickable(locator)
            Logger.add_end_step(method='Клик по чекбоксу без текста')


    def field_optional_filling(self, locator_field, field_name, send_keys):
        """ЗАПОЛНЕНИЕ НЕОБЯЗАТЕЛЬНЫХ ПОЛЕЙ ВВОДА"""
        with allure.step(f'Заполнение необязательных полей ввода {field_name}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Заполнение необязательных полей ввода {field_name}')
            name_field = self.element_to_be_clickable_without_click(locator_field)
            name_field.send_keys(Keys.CONTROL, 'a')
            name_field.send_keys(send_keys)

            assert name_field.get_attribute('value') == send_keys
            print(f"{field_name} {name_field.get_attribute('value')} - УСПЕШНО")
        Logger.add_end_step(method='Заполнение необязательных полей ввода')


    def add_photo(self, locator_field, link):
        """ДОБАВЛЕНИЕ ИЗОБРАЖЕНИЯ"""
        with allure.step(f'Добавление изображения {link}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Добавление изображения {link}')
            photo_add_button = self.element_to_be_clickable_without_click(locator_field)
            photo_add_button.send_keys(link)
            print("Изображение добавлено - УСПЕШНО")
            Logger.add_end_step(method='Добавление изображения')


    def check_element_in_page_false(self, locator, element_name):
        """ПРОВЕРКА ОТСУТСТВИЯ ЭЛЕМЕНТА"""
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


    def check_element_in_page_true(self, locator, element_name):
        """ПРОВЕРКА ПРИСУТСТВИЯ ЭЛЕМЕНТА"""
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


    def is_alert_present(self):
        """ПЕРЕКЛЮЧЕНИЕ НА МОДАЛЬНОЕ ОКНО С СООБЩЕНИЕМ"""
        with allure.step('Переключение на модальное окно с сообщением'):
            try:
                self.driver.switch_to_alert()
            except NoAlertPresentException:
                return False


    def get_screenshot(self):
        """СКРИНШОТ"""
        date_now = datetime.datetime.now().strftime("%d.%m.%Y_время_%H.%M.%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Screenshot{date_now}", attachment_type=AttachmentType.PNG)
        screenshot_name = f'Снимок {date_now}.jpeg'
        self.driver.save_screenshot(f"{os.getcwd()}\\screenshots\{screenshot_name}")


    def text_on_pages(self, locator, text_name):
        """ТЕКСТ НА СТРАНИЦАХ"""
        name_text = self.visibility_of_element_located(locator)
        with allure.step(f'Текст на страницах: "{name_text.text}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Текст на страницах: "{text_name}"')
            assert name_text.text == text_name
            print(f"{name_text.text} - УСПЕШНО")
            Logger.add_end_step(method='Текст на страницах')


    def list_dropdown_down_enter_choose(self, locator_field, locator_text):
        """ВЫБОР ИЗ ВЫПАДАЮЩЕГО СПИСКА"""
        with allure.step(f'Выбор из выпадающего списка "{locator_text}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Выбор из выпадающего списка')
            self.element_to_be_clickable(locator_field)
            time.sleep(1)
            self.element_to_be_clickable(locator_text)
            print(f'Значение выбрано - УСПЕШНО')
            Logger.add_end_step(method='Выбор из выпадающего списка')