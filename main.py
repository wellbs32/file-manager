
from CONFIG import QUICK_ACCESS, BASE_PATH
import functions

import os
import sys
import time

os.chdir(os.getcwd())
new_path = ''

while True:

    current_dir = os.getcwd()

    print(f'\nCurrent Directory: {current_dir}')

    # --- Function Selector ---

    # 1 = Quick Access
    # 2 = Directory Content
    # 3 = Access Directory
    # 4 = Rename
    # 5 = File Stats
    # 0 = Exit Program

    choose_func = functions.options_menu()

    if choose_func == '1':
        # change the directory

        new_path = functions.quick_access_path()

    elif choose_func == '2':
        # show the directory content

        functions.dir_content(new_path, BASE_PATH)

    elif choose_func == '3':
        # access any directory inside the current dir

        functions.access_dir()

    elif choose_func == '4':

        functions.go_back_dir()

    elif choose_func == '5':
        # rename the directory or file

        functions.rename()

    elif choose_func == '6':

        functions.file_stats()

    elif choose_func == '7':

        functions.create_file_dir(current_dir)

    elif choose_func == '8':

        functions.remove_file_dir(current_dir)

    elif choose_func == '9':
        # exit program

        sys.exit()

    else:
        print('\nInsert a valid number.')
