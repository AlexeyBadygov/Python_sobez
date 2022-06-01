"""
Реализовать функцию print_directory_contents(path). Функция принимает имя директории и выводит ее содержимое,
включая содержимое всех поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно
использовать os.listdir и os.path.isfile
"""
import os


def print_directory_contents(path):
    """
    Функция (рекурсивная) вывода содержимого директорий
    :param path:
    :return:
    """
    for item in os.listdir(path):
        inside_dir = os.path.join(path, item)
        print(inside_dir)
        if os.path.isdir(inside_dir):
            print_directory_contents(inside_dir)


print_directory_contents(os.getcwd())
