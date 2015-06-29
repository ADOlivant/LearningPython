from animal_class import *

class Sheep(Animal):
	"""A Sheep"""
	def __init__(self, arg):
		#call the parent / super class constructor with default values for Sheep
		#growth rate = 1; food need = 3; water need = 6
		super().__init__(1,3,6)
		self.type = "Sheep"

	#override grow method for subclass
	def grow(self,food,water):
		if food >= self._light_need and water >= self._water_need:
			if self._status == "Baby" and water > self._water_need:
				self._growth += self._growth_rate * 1.25
			elif self._status == "Young" and water > self._water_need:
				self._growth += self._growth_rate * 1.175
			elif self._status == "Mature" and water > self._water_need: 
				self._growth += self._growth_rate / 2
			else: 
				self._growth += self._growth_rate
		#increment days growing
		self._days_growing += 1
		#update the status
		self._update_status()

def main():
	#create a new Sheep animal
	sheep_animal = Sheep()
	print(sheep_animal.report())
	#manually grow the animal
	manual_grow(sheep_animal)
	print(sheep_animal.report())

if __name__ == "__main__":
	main()