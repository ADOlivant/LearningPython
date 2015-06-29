from animal_class import *

class Cow(Animal):
	"""A cow"""
	def __init__(self, arg):
		#call the parent / super class constructor with default values for cow
		#growth rate = 1; food need = 3; water need = 6
		super().__init__(1,3,6)
		self.type = "Cow"

	#override grow method for subclass
	def grow(self,food,water):
		if food >= self._light_need and water >= self._water_need:
			if self._status == "Baby" and water > self._water_need:
				self._growth += self._growth_rate * 1.5
			elif self._status == "Young" and water > self._water_need:
				self._growth += self._growth_rate * 1.25
			else: 
				self._growth += self._growth_rate
		#increment days growing
		self._days_growing += 1
		#update the status
		self._update_status()

def main():
	#create a new cow animal
	cow_animal = Cow()
	print(cow_animal.report())
	#manually grow the animal
	manual_grow(cow_animal)
	print(cow_animal.report())

if __name__ == "__main__":
	main()