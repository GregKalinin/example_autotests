import time
import allure
from allure import severity, severity_level
from base.base_class import BaseData
from page.methods import Methods
from base.locators import Locators

class Test_Student_Registration_Form:

    """РЕГИСТРАЦИЯ СТУДЕНТА"""
    @allure.description('РЕГИСТРАЦИЯ СТУДЕНТА')
    @severity(severity_level.CRITICAL)
    def test_student_registration_form(self):

        Methods.browser_open_chrome(self)

        try:

            # Прокрутка страницы вниз
            Methods(self.driver).scrolling_page_down()

            # Переход в модуль "Формы"
            Methods(self.driver).element_to_be_clickable(Locators.FORMS_MODULE)

            # Переход на страницу регистрации студента
            Methods(self.driver).element_to_be_clickable(Locators.STUDENT_REG_FORM)

            # Проверка названия страницы
            Methods(self.driver).text_on_pages(Locators.TITLE_NAME_STUDENT_REG_FORM, 'Student Registration Form')

            # Поле ввода "Имя"
            Methods(self.driver).field_optional_filling(Locators.FIRST_NAME_FIELD_STUDENT_REG_FORM, 'Имя:', BaseData.first_name_student)

            # Поле ввода "Фамилия"
            Methods(self.driver).field_optional_filling(Locators.LAST_NAME_FIELD_STUDENT_REG_FORM, 'Фамилия:', BaseData.last_name_student)

            # Поле ввода "Email"
            Methods(self.driver).field_optional_filling(Locators.EMAIL_FIELD_STUDENT_REG_FORM, 'Email:', BaseData.email_student)

            # Выбор пола
            Methods(self.driver).radio_button_click(Locators.MALE_RADIO_BUTTON_STUDENT_REG_FORM)

            # Поле ввода "Мобильный номер"
            Methods(self.driver).field_optional_filling(Locators.MOBILE_NUMBER_FIELD_STUDENT_REG_FORM, 'Мобильный номер:',
                                                        BaseData.mobile_number_student)

            # Поле ввода "Дата рождения"
            Methods(self.driver).field_optional_filling(Locators.DATE_OF_BIRTH_FIELD_STUDENT_REG_FORM, 'Дата рождения:',
                                                        BaseData.date_of_birth_student)

            # Поле ввода "Предметы"
            Methods(self.driver).field_optional_filling(Locators.SUBJECTS_FIELD_STUDENT_REG_FORM, 'Предметы:',
                                                        BaseData.subject_student)

            # Клик по чекбоксу "Хобби"
            Methods(self.driver).checkbox_click_without_text(Locators.RANDOM_CHECKBOX_STUDENT_REG_FORM)

            # Добавление изображения
            Methods(self.driver).add_photo(Locators.ADD_PICTURE_STUDENT_REG_FORM, BaseData.link_add_picture_student)

            # Прокрутка страницы вниз
            Methods(self.driver).scrolling_page_down()

            # Поле ввода "Текущий адрес"
            Methods(self.driver).field_optional_filling(Locators.CURRENT_ADDRESS_FIELD_STUDENT_REG_FORM, 'Текущий адрес:',
                                                        BaseData.current_address_student)

            # Выбор штата
            Methods(self.driver).list_dropdown_down_enter_choose(Locators.STATE_LIST_STUDENT_REG_FORM,
                                                                 Locators.STATE_LIST_HARYANA_NAME_STUDENT_REG_FORM)

            # Выбор города
            Methods(self.driver).list_dropdown_down_enter_choose(Locators.CITY_LIST_STUDENT_REG_FORM,
                                                                 Locators.CITY_LIST_KARNAL_NAME_STUDENT_REG_FORM)

            # Проверка текста в футере
            Methods(self.driver).text_on_pages(Locators.FOOTER_TEXT,
                                               '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')

        finally:
            Methods.get_screenshot(self)
            time.sleep(2)
            self.driver.quit()