from random import randint

from selenium.webdriver.common.by import By


class Locators:

    """Класс с локаторами"""
    # Раздел "Формы"
    FORMS_MODULE = (By.XPATH, "//h5[text()='Forms']")
    # Страница регистрации студента
    STUDENT_REG_FORM = (By.XPATH, "//span[text()='Practice Form']")
    # Заголовок страницы "Форма регистрации студента"
    TITLE_NAME_STUDENT_REG_FORM = (By.XPATH, "//h5[text()='Student Registration Form']")
    # Поле "Имя"
    FIRST_NAME_FIELD_STUDENT_REG_FORM = (By.ID, 'firstName')
    # Поле "Фамилия"
    LAST_NAME_FIELD_STUDENT_REG_FORM = (By.ID, 'lastName')
    # Поле "Эл. почта"
    EMAIL_FIELD_STUDENT_REG_FORM = (By.ID, 'userEmail')
    # Выбор пола
    MALE_RADIO_BUTTON_STUDENT_REG_FORM = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    FEMALE_RADIO_BUTTON_STUDENT_REG_FORM = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    OTHER_RADIO_BUTTON_STUDENT_REG_FORM = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    # Поле "Мобильный номер"
    MOBILE_NUMBER_FIELD_STUDENT_REG_FORM = (By.ID, 'userNumber')
    # Поле "Дата рождения"
    DATE_OF_BIRTH_FIELD_STUDENT_REG_FORM = (By.ID, 'dateOfBirthInput')
    # Поле "Предметы"
    SUBJECTS_FIELD_STUDENT_REG_FORM = (By.ID, 'subjectsInput')
    # Выбор хобби
    RANDOM_CHECKBOX_STUDENT_REG_FORM = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{randint(1, 3)}']")
    # Кнопка добавления изображения
    ADD_PICTURE_STUDENT_REG_FORM = (By.ID, 'uploadPicture')
    # Поле "Текущий адрес"
    CURRENT_ADDRESS_FIELD_STUDENT_REG_FORM = (By.ID, 'currentAddress')
    # Выпадающий список выбор штата
    STATE_LIST_STUDENT_REG_FORM = (By.ID, 'state')
    # Название штата
    STATE_LIST_HARYANA_NAME_STUDENT_REG_FORM = (By.XPATH, "//div[text()='Haryana']")
    # Выпадающий список выбор города
    CITY_LIST_STUDENT_REG_FORM = (By.ID, 'city')
    # Название города
    CITY_LIST_KARNAL_NAME_STUDENT_REG_FORM = (By.XPATH, "//div[text()='Karnal']")
    # Текст в футере
    FOOTER_TEXT = (By.XPATH, "//span[text()='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.']")