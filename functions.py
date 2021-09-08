from CONFIG import QUICK_ACCESS

import os
import sys
import time


def options_menu():
    print('''
 ##########################################################################
#                                                                          #
# OPTIONS: Quick Access [1] | Dir Content [2] | Enter Dir [3] | Rename [4] #
#                                                                          #
############################################################################
#                                                                          #
# | Properties [5] | Exit [0] |                                            #
#                                                                          #
 ##########################################################################
		''')

    print('What do you want to do?')
    choose_func = input()
    return choose_func


def quick_access_path():
    print('\nQuick Access: | Users | Desktop | Documents | Downloads |\n')

    print('What directory do you want access?')
    new_path = input()

    try:
        os.chdir(QUICK_ACCESS[new_path])
        return new_path
    except KeyError:
        print('Insert a valid name.')


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
        print(f'Size: {file_size / 1000} KB')
        print(f'Extension: {file_get_extension[-1]}')

    except FileNotFoundError:
        print("File doesn't exists.")
