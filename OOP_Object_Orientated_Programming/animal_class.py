import random

class Animal:
	"""A generic animal"""

	#constructor
	def __init__(self, growth_rate, food_need, water_need, name):
		#set the attributes with initial value

		self._weight = 0
		self._days_growing = 0
		self._growth_rate = growth_rate
		self._food_need = food_need
		self._water_need = water_need
		self._status = "Baby"
		self._type = "Generic"
		self._name = ""
		
		#the above attributes are prefixed with an underscore to indicate 
		#that they should not be accessed directly from out with the class
		
	#method to indicate the needs of the animal 
	def needs(self): 
		#return a dictionary containing the light and water needs
		return {'food need': self._food_need, 'water need': self._water_need}

	#method to report the provided information about the current state of the 
	#animal
	def report(self): 
		#return a dictionary containing the type, growth, and days growing
		return {'name': self._name, 'type': self._type, 'status':self._status, 'weight':self._weight, 'days growing':self._days_growing}

	#the underscore indicates that this method should not be called from out with 
	#the class
	def _update_status(self):
		#update the status of the animal based on the growth
		if self._weight > 15: 
			self._status = "Old"
		elif self._weight > 10: 
			self._status = "Mature"
		elif self._weight > 5: 
			self._status = "Young"
		elif self._weight == 0: 
			self._status = "Baby"

	def grow(self,food,water): 
		#grow the animal dependent on the food and water available and need and to 
		#update the required attributes if completed.
		if food >= self._food_need and water >= self._water_need: 
			self._weight += self._growth_rate
		#increment days growing
		self._days_growing += 1
		#update the status
		self._update_status()

	def name_animal(self,name): 
		self._name = name

def auto_grow(animal,days):
	#grow the animal 
	for day in range(days): 
		food = random.randint(1,10)
		water = random.randint(1,10)
		animal.grow(food,water)

def manual_grow(animal):
	#get the food and water values from the user
	valid = False
	while not valid: 
		try: 
			food = int(input("Please enter a food value (1-10): "))
			if 1 <= light <= 10: 
				valid = True
			else: 
				print("Value entered not valid - please enter a value between 1 and 10")
		except ValueError:
			print("Value entered not valid - please enter a value between 1 and 10")
	valid = False
	while not valid: 
		try: 
			water = int(input("Please enter a water value (1-10): "))
			if 1 <= water <= 10: 
				valid = True
			else: 
				print("Value entered not valid - please enter a value between 1 and 10")
		except ValueError:
			print("Value entered not valid - please enter a value between 1 and 10")
	#grow the animal
	animal.grow(food,water)

def display_menu(): 
	#function to display menu choices when it is called. 
	print("1. Grow manually over 1 day")
	print("2. Grow automatically over 30 days")
	print("3. Report status")
	print("0. Exit test program")
	print()
	print("Please select an option from the above menu")

def get_menu_choice():
	#function to get a menu choice from the user.
	option_valid = False
	while not option_valid:
		try: 
			choice = int(input("Option Selected:"))
			if 0 <= choice <= 3: 
				option_valid = True
			else: 
				print("Please enter a valid option")
		except ValueError: 
			print("Please enter a valid option")
	return choice

def manage_animal(animal):
	print("This is the animal management program")
	print()
	noexit = True
	while noexit: 
		display_menu()
		option = get_menu_choice()
		print()

		if option == 1:
			manual_grow(animal)
			print()
		elif option == 2: 
			auto_grow(animal,30)
			print()
		elif option == 3: 
			print(animal.report())
			print()
		elif option == 0: 
			noexit = False
			print()
	print("Thank you for using the animal management program")

def main(): 
	#instantiate the class
	new_animal = Animal(1,4,3)
	manage_animal(new_animal)

if __name__ == "__main__":
	main()