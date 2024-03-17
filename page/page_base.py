import datetime
import os
import allure
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from allure_commons.types import AttachmentType


class Page_Base:

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



    def button_double_click(self, locator):
        """ДВОЙНОЙ КЛИК ПО КНОПКЕ"""
        variable_button = self.element_to_be_clickable_without_click(locator)
        with allure.step('Двойной клик по кнопке'):
            for i in range(2):
                variable_button.click()


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