from page.page_base import Page_Base
import time
import allure
from selenium.webdriver import Keys
from utilities.logger import Logger

class Page_Registration(Page_Base):


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