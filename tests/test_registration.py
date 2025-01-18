import allure
import pytest
from allure import severity, severity_level

from base.base_class import BaseData
from base.locators import Locators
from page.basepage import BasePage
from page.page_registration import RegistrationPage


@allure.feature("Функционал регистрации студента")
class TestStudentRegistrationForm(BaseData):

    @allure.title('Регистрация студента')
    @allure.description('Страница регистрации студента')
    @severity(severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @pytest.mark.parametrize('settings', [BaseData.settings_for_student_registration])
    def test_student_registration_form(self, settings, open_browsers):
        create_page = RegistrationPage(open_browsers)

        try:

            # Прокрутка страницы вниз
            create_page.scrolling_page(0, 600)

            # Переход в модуль "Формы"
            create_page.element_to_be_clickable(Locators.FORMS_MODULE)

            # Переход на страницу регистрации студента
            create_page.element_to_be_clickable(Locators.STUDENT_REG_FORM)

            # Проверка названия страницы
            create_page.text_on_pages(Locators.TITLE_NAME_STUDENT_REG_FORM, 'Student Registration Form')

            # Поле ввода "Имя"
            create_page.field_optional_filling(Locators.FIRST_NAME_FIELD_STUDENT_REG_FORM,
                                               'Имя:', settings.get('first_name_student'))

            # Поле ввода "Фамилия"
            create_page.field_optional_filling(Locators.LAST_NAME_FIELD_STUDENT_REG_FORM,
                                               'Фамилия:', settings.get('last_name_student'))

            # Поле ввода "Email"
            create_page.field_optional_filling(Locators.EMAIL_FIELD_STUDENT_REG_FORM,
                                               'Email:', settings.get('email_student'))

            # Выбор пола
            create_page.radio_button_click(Locators.MALE_RADIO_BUTTON_STUDENT_REG_FORM)

            # Поле ввода "Мобильный номер"
            create_page.field_optional_filling(Locators.MOBILE_NUMBER_FIELD_STUDENT_REG_FORM,
                                               'Мобильный номер:', settings.get('mobile_number_student'))

            # Поле ввода "Дата рождения"
            create_page.field_optional_filling(Locators.DATE_OF_BIRTH_FIELD_STUDENT_REG_FORM,
                                               'Дата рождения:', settings.get('date_of_birth_student'))

            # Поле ввода "Предметы"
            create_page.field_optional_filling(Locators.SUBJECTS_FIELD_STUDENT_REG_FORM,
                                               'Предметы:', settings.get('subject_student'))

            # Клик по чекбоксу "Хобби"
            create_page.checkbox_click_without_text(Locators.RANDOM_CHECKBOX_STUDENT_REG_FORM)

            # Добавление изображения
            create_page.add_photo(Locators.ADD_PICTURE_STUDENT_REG_FORM,
                                  settings.get('link_add_picture_student'))

            # Прокрутка страницы вниз
            create_page.scrolling_page(0, -600)

            # Поле ввода "Текущий адрес"
            create_page.field_optional_filling(Locators.CURRENT_ADDRESS_FIELD_STUDENT_REG_FORM,
                                               'Текущий адрес:', settings.get('current_address_student'))

            # Выбор штата
            create_page.list_dropdown_down_enter_choose(Locators.STATE_LIST_STUDENT_REG_FORM,
                                                                 Locators.STATE_LIST_HARYANA_NAME_STUDENT_REG_FORM)

            # Выбор города
            create_page.list_dropdown_down_enter_choose(Locators.CITY_LIST_STUDENT_REG_FORM,
                                                                 Locators.CITY_LIST_KARNAL_NAME_STUDENT_REG_FORM)

            # Проверка текста в футере
            create_page.text_on_pages(Locators.FOOTER_TEXT,
                                               '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')

        finally:

            # Скриншот страницы
            BasePage.get_screenshot(self)