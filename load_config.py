import os
from dotenv import load_dotenv

VERSION = '1.00'


def check_config_file():
    if not os.path.isfile(os.path.join(os.getcwd(), 'config.env')):
        create_config_file()


def create_config_file():
    print('Файл отсутствует')


if __name__ == '__main__':
    check_config_file()