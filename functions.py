from CONFIG import QUICK_ACCESS

import os

def quick_access_box():
	print('''
 _________________________________________
| 										  |
|				Quick Access 			  |
|_________________________________________|
|		|		  |			  |			  |
| Users | Desktop | Documents | Downloads |
|_______|_________|___________|___________|
		''')

def change_path():
	quick_access_box()

	while True:



		print('What directory do you want access?')
		quick_path = input()

		try:
			os.chdir(str(QUICK_ACCESS[quick_path]))
			return quick_path
		except KeyError:
			print('Insert a valid name.')

		


def dir_content(path):
	print('')
	for name in os.listdir():
		path_name = os.path.join(QUICK_ACCESS[path], name)
		if os.path.isfile(path_name):
			print(f'File | {name}')
		elif os.path.isdir(path_name):
			print(f'Dir  | {name}')
		else:
			print(name)
	print('')