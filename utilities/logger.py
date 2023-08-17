import datetime
import os
import requests


class Logger:

    file_name = f"{os.getcwd()}\\logs\log_{str(datetime.datetime.now().strftime('%d.%m.%Y_время_%H.%M.%S'))}.log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"ТЕСТ: {test_name}\n"
        data_to_add += f"ВРЕМЯ НАЧАЛА: {str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))}\n"
        data_to_add += f"ЗАПУСК МЕТОДА: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"Ответ: {requests.get(url).status_code}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, method: str):
        data_to_add = f"ВРЕМЯ ЗАВЕРШЕНИЯ: {str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))}\n"
        data_to_add += f"ЗАВЕРШЕНИЕ МЕТОДА: {method}\n"
        data_to_add += f"-----\n"

        cls.write_log_to_file(data_to_add)