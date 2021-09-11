from CONFIG import QUICK_ACCESS

import os
import sys
import time


def show_options():
    print('\nWrite 0 to show the options:')
    write_value = input()

    if write_value == '0':
        return True
    else:
        return False


def options_menu():
    options_answer = show_options()

    if options_answer:
        print('''
     ##############################################################################
    #                                                                              #
    # OPTIONS: Quick Access [1] | Dir Content [2] | Enter Dir [3] | Return Dir [4] #
    #                                                                              #
    ###############################################################################
    #                                                                              #
    #    Rename [5] | Properties [6] | Create File/Dir [7] | Remove File/Dir [8]   #
    #                                                                              #
    ################################################################################
    #                                                                              #
    #                                   Exit [9]                                   #
    #                                                                              #
     ##############################################################################
            ''')

        print('What do you want to do?')
        choose_func = input()
        return choose_func
    else:
        pass


def quick_access_path():
    print('\nQuick Access: | Home | Desktop | Documents | Downloads |')

    print('\nWhat directory do you want access?')
    new_path = input()

    try:
        os.chdir(QUICK_ACCESS[new_path])
        return new_path
    except KeyError:
        print('\nInsert a valid name.')


def dir_content(path, base):
    print('')

    for name in os.listdir():

        if path == '':
            path_name = os.path.join(base, name)
        else:
            path_name = os.path.join(QUICK_ACCESS[path], name)

        if os.path.isfile(path_name):
            print(f'File | {name}')
        elif os.path.isdir(path_name):
            print(f'Dir  | {name}')
        else:
            print(name)
    print('')


def access_dir():
    print('\nSelect one directory inside the current directory.')

    path_dir = input()

    new_path = os.path.join(os.getcwd(), path_dir)
    if os.path.exists(new_path):
        os.chdir(new_path)
    else:
        print('\nInsert a correct dir name.')


def go_back_dir():
    split_path = os.path.split(os.getcwd())

    os.chdir(split_path[0])


def rename():
    print('\nWhich file do you want to rename?')
    file_name = input()

    print('\nInsert the new name of the file:')
    new_file_name = input()

    try:
        os.rename(file_name, new_file_name)
    except FileExistsError:
        print('\nThis name already exists.')
    except FileNotFoundError:
        print("\nThis file doesn't exists.")


def file_stats():
    print('\nSelect a file to see the properties.')

    try:
        file_name = input()

        file_size = os.stat(file_name).st_size
        file_last_time = os.stat(file_name).st_mtime
        file_get_extension = os.path.splitext(file_name)

        print('\nFile Properties')
        print('-------------------')
        print(f'Last Modification: {time.ctime(file_last_time)}')
        print(f'Size: {(file_size / 1000):,} KB')
        print(f'Extension: {file_get_extension[-1]}')

    except FileNotFoundError:
        print("\nFile doesn't exists.")


def call_file_dir(path):
    print('\nWrite the name of the file:')
    file_name = input()

    return os.path.join(path, file_name)


def create_file_dir(path):
    file_path = call_file_dir(path)
    check_extension = os.path.splitext(file_path)

    if check_extension[-1] == '':
        os.mkdir(file_path)
    else:
        with open(file_path, 'a'):
            os.utime(path, None)


def remove_file_dir(path):
    file_path = call_file_dir(path)

    try:
        os.remove(file_path)
    except (PermissionError, IsADirectoryError):
        os.rmdir(file_path)
    except FileNotFoundError:
        print("File or Dir doens't exists.")
