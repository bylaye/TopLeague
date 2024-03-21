import configparser
import os
import sys
from requests import get
from datetime import date, datetime


absolute_dir_path_file = os.path.abspath(os.path.dirname(__file__))


"""Get absolute path to store directory"""
def absolute_path_directory_data(name):
    path_dir = os.path.join(absolute_dir_path_file, name)
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)
    return path_dir


"""check and Get config file"""
def check_config_file():
    path_dir = os.path.join(absolute_dir_path_file, 'config')
    filename = os.path.join(path_dir, 'config.ini')
    if os.path.isfile(filename):
        return filename
    else:
        print(f"config file {filename} don't exists")
        exit(1)


if __name__ == '__main__':
    config_file = check_config_file()
    config = configparser.ConfigParser()
    config.read(config_file)
    dirname_data = config.get('dirs', 'DIRNAME_DATA_EXTRACT')
    dir_data_extract = absolute_path_directory_data(dirname_data)
    print(f'data path = {dir_data_extract}')