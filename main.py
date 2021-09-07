from CONFIG import QUICK_ACCESS 
import functions

import os

os.chdir('C:/')


while True:

	quick_path = functions.change_path()

	print(f'\nCurrent Directory: {os.getcwd()}')


	functions.dir_content(quick_path)