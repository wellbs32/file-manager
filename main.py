from CONFIG import QUICK_ACCESS, BASE_PATH
import functions

import os
import sys
import time

os.chdir(BASE_PATH)
new_path = ''

while True:

    print(f'\nCurrent Directory: {os.getcwd()}')

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
        # rename the directory or file

        functions.rename()

    elif choose_func == '5':

        functions.file_stats()

    elif choose_func == '0':
        # exit program

        sys.exit()

    else:
        print('Insert a valid number.')
