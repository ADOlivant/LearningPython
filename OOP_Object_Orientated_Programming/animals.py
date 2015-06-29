from cow_class import *
from sheep_class import *

def display_menu(): 
	print()
	print("Which animal would you like to create")
	print()
	print("1. Cow")
	print("2. Sheep")
	print()
	print("Please select an option from the above menu")

def select_option(): 
	#function to get a menu choice from the user.
	valid_option = False
	while not valid_option:
		try: 
			choice = int(input("Option Selected:"))
			if 0 <= choice <= 3: 
				valid_option = True
			else: 
				print("Please enter a valid option")
		except ValueError: 
			print("Please enter a valid option")
	return choice

def get_name(): 
	#function to name the animal which will be created.
	print()
	name = input("Please enter a name for the animal: ")
	return name

def create_crop(): 
	display_menu()
	choice = select_option()
	name = get_name()
	if choice == 1: 
		new_crop = Potato()
		new_crop.name_animal(name)
	elif choice == 2: 
		new_crop = Wheat()
		new_crop.name_animal(name)
	return new_crop

def main(): 
	new_crop = create_crop()
	manage_crop(new_crop)

if __name__ == "__main__": 
	main()