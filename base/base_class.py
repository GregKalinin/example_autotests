import os
import random
from base.change_names import NamesChange


class BaseData():

    """ФОРМА РЕГИСТРАЦИИ СТУДЕНТА"""
    first_name_student = random.choice(NamesChange.list_first_name_stud)
    last_name_student = random.choice(NamesChange.list_last_name_stud)
    email_student = random.choice(NamesChange.list_email_stud)
    mobile_number_student = random.choice(NamesChange.list_mobile_number_stud)
    date_of_birth_student = random.choice(NamesChange.list_date_of_birth_stud)
    subject_student = random.choice(NamesChange.list_subject_stud)
    link_add_picture_student = f"{os.getcwd()}\\files_for_tests\demoqa.jpg"
    current_address_student = 'город Москва, улица Ленина 100, кв. 100, индекс 111111'
