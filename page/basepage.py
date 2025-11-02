import datetime
import os

import allure
from allure_commons.types import AttachmentType
from selenium.common import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from utilities.logger import Logger


class BasePage:

    """Базовый класс"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 10, poll_frequency=1)

    def element_to_be_clickable(self, locator):
        """
        Метод с ожиданием кликабельности и кликом
        :param locator: Локатор элемента
        Возвращает объект WebElement
        """
        return wait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator)).click()

    def element_to_be_clickable_without_click(self, locator):
        """
        Метод с ожиданием кликабельности без клика
        :param locator: Локатор элемента
        Возвращает объект WebElement
        """
        return wait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator))

    def visibility_of_element_located(self, locator):
        """
        Отображение элемента
        :param locator: Локатор элемента
        Возвращает объект WebElement
        """
        return wait(self.driver, 20, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def presence_of_element_located(self, locator):
        """
        Ожидание наличия элемента
        :param locator: Локатор элемента
        Возвращает объект WebElement
        """
        return wait(self.driver, 20, poll_frequency=1).until(EC.presence_of_element_located(locator))

    def get_current_url(self):
        """Получение текущего url"""
        get_url = self.driver.current_url
        print('Текущий URL:', + get_url)

    def authorization(self, login_field, password_field, locator_login, locator_pass, locator_button):
        """
        Авторизация
        :param login_field: Имя пользователя
        :param password_field: Пароль
        :param locator_login: Локатор поля имени пользователя
        :param locator_pass: Локатор поля пароля
        :param locator_button: Локатор кнопки 'Войти"
        """
        with allure.step('Авторизация'):
            Logger.add_start_step(url=self.driver.current_url, method='Авторизация')
            self.element_to_be_clickable_without_click(locator_login).send_keys(login_field)
            self.element_to_be_clickable_without_click(locator_pass).send_keys(password_field)
            self.element_to_be_clickable(locator_button)
            Logger.add_end_step(method='Авторизация')

    def scrolling_page(self, x: int = 0, y: int = 0):
        """
        Прокрутка страницы
        :param x: Значение по оси x
        :param y: Значение по оси y
        """
        with allure.step('Прокрутка страницы'):
            self.driver.execute_script(f"window.scrollBy({x}, {y})")

    def button_double_click(self, locator):
        """
        Двойной клик по кнопке
        :param locator: Локатор элемента
        """
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Двойной клик по кнопке'):
            for i in range(2):
                variable_button.click()

    def is_alert_present(self):
        """Переключение на модальное окно с сообщением"""
        with allure.step('Переключение на модальное окно с сообщением'):
            try:
                self.driver.switch_to_alert()
            except NoAlertPresentException:
                return False

    def get_screenshot(self):
        """Скриншот"""
        date_now = datetime.datetime.now().strftime("%d.%m.%Y_время_%H.%M.%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Screenshot{date_now}", attachment_type=AttachmentType.PNG)
        screenshot_name = f'Снимок {date_now}.jpeg'
        self.driver.save_screenshot(f"{os.getcwd()}\\tests\\screenshots\\{screenshot_name}")
