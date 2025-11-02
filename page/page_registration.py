import time

import allure
from selenium.webdriver import Keys

from page.basepage import BasePage
from utilities.logger import Logger


class RegistrationPage(BasePage):

    """Класс с методами для страницы регистрации"""

    def check_link_click(self, locator, text_value):
        """
        Название ссылки и клик
        :param locator: Локатор элемента
        :param text_value: Текст ссылки
        """
        variable_link = self.visibility_of_element_located(locator)
        with allure.step(f'Название ссылки {text_value}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Название ссылки {text_value}')
            error_text = f"Ожидаемое: '{text_value}', текущее: '{variable_link.text}'"
            assert variable_link.text == text_value, error_text
            variable_link.click()
            Logger.add_end_step(method='Название ссылки')

    def button_click(self, locator, button_text):
        """
        Клик по кнопке
        :param locator: Локатор элемента
        :param button_text: Название кнопки
        """
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Клик по кнопке {button_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Клик по кнопке, проверка названия кнопки {button_text}')
            error_text = f"Ожидаемое: '{button_text}', текущее: '{variable_button.text}'"
            assert variable_button.text == button_text, error_text
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке, проверка названия кнопки')

    def button_without_click(self, locator, button_text):
        """
        Без клика по кнопке
        :param locator: Локатор элемента
        :param button_text: Название кнопки
        """
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Без клика по кнопке {button_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Без клика по кнопке, проверка названия кнопки{button_text}')
            error_text = f"Ожидаемое: '{button_text}', текущее: '{variable_button.text}'"
            assert variable_button.text == button_text, error_text
            Logger.add_end_step(method='Без клика по кнопке, проверка названия кнопки')

    def button_click_without_check_name(self, locator):
        """
        Клик по кнопке без проверки названия
        :param locator: Локатор элемента
        """
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')

    def radio_button_click(self, locator):
        """
        Клик по радио кнопке
        :param locator: Локатор элемента
        """
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Клик по кнопке без проверки названия'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по кнопке без проверки названия')
            variable_button.click()
            Logger.add_end_step(method='Клик по кнопке без проверки названия')

    def checkbox_click(self, locator, checkbox_text):
        """
        Клик по чекбоксу
        :param locator: Локатор элемента
        :param checkbox_text: Название чек-бокса
        """
        variable_checkbox = self.element_to_be_clickable_without_click(locator)
        with allure.step(f'Клик по чекбоксу {checkbox_text}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Клик по чекбоксу {checkbox_text}')
            error_text = f"Ожидаемое: '{checkbox_text}', текущее: '{variable_checkbox.text}'"
            assert variable_checkbox.text == checkbox_text, error_text
            variable_checkbox.click()
            Logger.add_end_step(method='Клик по чекбоксу')

    def checkbox_click_without_text(self, locator):
        """
        Клик по чекбоксу без текста
        :param locator: Локатор элемента
        """
        with allure.step('Клик по чекбоксу без текста'):
            Logger.add_start_step(url=self.driver.current_url, method='Клик по чекбоксу без текста')
            self.element_to_be_clickable(locator)
            Logger.add_end_step(method='Клик по чекбоксу без текста')

    def field_optional_filling(self, locator_field, field_name, send_keys, esc_button=False, tab_button=False):
        """
        Заполнение необязательных полей ввода
        :param locator_field: Локатор элемента
        :param field_name: Название поля ввода
        :param send_keys: Текст для ввода
        :param esc_button: Нажать ESCAPE
        :param tab_button: Нажать TAB
        """
        with allure.step(f'Заполнение необязательных полей ввода {field_name}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Заполнение необязательных полей ввода {field_name}')
            name_field = self.element_to_be_clickable_without_click(locator_field)
            name_field.send_keys(Keys.CONTROL, 'a')
            name_field.send_keys(send_keys)
            error_text = f"Ожидаемое: '{send_keys}', текущее: '{name_field.get_attribute('value')}'"
            assert name_field.get_attribute('value') == send_keys, error_text
            if esc_button:
                name_field.send_keys(Keys.ESCAPE)
            if tab_button:
                time.sleep(2)
                name_field.send_keys(Keys.TAB)
            Logger.add_end_step(method='Заполнение необязательных полей ввода')

    def add_photo(self, locator_field, link):
        """
        Добавление изображения
        :param locator_field: Локатор элемента
        :param link: Ссылка
        """
        with allure.step(f'Добавление изображения {link}'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Добавление изображения {link}')
            photo_add_button = self.element_to_be_clickable_without_click(locator_field)
            photo_add_button.send_keys(link)
            Logger.add_end_step(method='Добавление изображения')

    def text_on_pages(self, locator, text_name):
        """
        Текст на страницах
        :param locator: Локатор элемента
        :param text_name: Ожидаемый текст
        """
        name_text = self.visibility_of_element_located(locator)
        with allure.step(f'Текст на страницах: "{name_text.text}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Текст на страницах: "{text_name}"')
            error_text = f"Ожидаемое: '{text_name}', текущее: '{name_text.text}'"
            assert name_text.text == text_name, error_text
            Logger.add_end_step(method='Текст на страницах')

    def list_dropdown_down_enter_choose(self, locator_field, locator_text):
        """
        Выбор из выпадающего списка
        :param locator_field: Локатор элемента
        :param locator_text: Текст в выпадающем списке
        """
        with allure.step(f'Выбор из выпадающего списка "{locator_text}"'):
            Logger.add_start_step(url=self.driver.current_url, method=f'Выбор из выпадающего списка')
            self.element_to_be_clickable(locator_field)
            time.sleep(1)
            self.element_to_be_clickable(locator_text)
            Logger.add_end_step(method='Выбор из выпадающего списка')
