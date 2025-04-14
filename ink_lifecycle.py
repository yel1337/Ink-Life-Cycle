from datetime import date


class NoInkError(Exception):
	def __init__(self):
		self.message = "Low in Ink or No Ink left!"
		super().__init__(self.message)

class LowOnInkError(Exception):
	def __init__(self):
		self.low_on_ink_warning = "Ink Running Low!"
		super().__init__(self.low_on_ink_warning)

class ReservoirError(Exception):
	def __init__(self):
		self.reservoir_message = "Reservoir not yet attached!"
		self.reservoir_warning = f"Error: {self.reservoir_message}"
		super().__init__(self.reservoir_warning)

class Ink():
	def __init__(self, when_bought):
		self.ink_level = 100
		self.when_bought = when_bought
		self.current_date = date.today() # Gives the current date
		self.total_decrement = 1 # By Default

		
	# A Method which determine the level of Ink from the day it was bought
	def _total_worn_(self):
	    days_passed = (self.current_date - self.when_bought).days
	    self.total_decrement += days_passed
	    return self.total_decrement  


	def _worn_(self):
		current_ink = len(self.total_decrement - self.ink_level)
		return current_ink 

		
	# If has Ink
	def has_ink(self):
		ink = self._worn_()
		if ink:
			return True
		else:
			return False


	def absorb_ink(self):
		try:
			if self.has_ink() == False:
				raise NoInkError()
		except NoInkError as e:
			print(f"{e}")
			return False 	


class Reservoir(Ink):
	"""
	Also houses the methods and object of Reservoir replica

	From getting the ink to checking the ink from the reservoir if running low
	"""
	def __init__(self):
		self.ink = Ink._worn_()
	 
	def get_ink(self):
		reservoir_with_ink = self.ink

		try:
			if not reservoir_with_ink:
				raise NoInkError
		except NoInkError as e:
			print(f"{e}")
			return False
		else:
			return True 

	def check_ink(self):
		try: 
			if self.ink < 10:
				raise NoInkError
		except NoInkError as e:
			print(f"{e}")
			return False
		else: 
			return True
		

	def using_ink(self):
		try:
			if self.check_ink() == True:
				current_running_ink = self.ink
				left_ink = 0
			
			for left_ink in range(self.ink): 
				current_running_ink -= self.total_decrement
			left_ink = current_running_ink
			
			if left_ink:
				return True 
			else:
				raise NoInkError
		except NoInkError as e: 
			print(f"{e}") 

	def _low_(self):
		try:
			self.check_ink()
		except NoInkError:
			raise LowOnInkError

	def check(self,
			  has_ink,
			  check_ink):
		if self.has_ink() and self.check_ink():
			return True
		else:
			return False 


class Barrel(Reservoir):
	def __init__(self):
		self.barrel_material = "Polypropylene"
		self.barrel_length = 15 # 15 cm 
		self.barrel_diameter = 1.5 #1.5 cm
		self.cap = None
		self.check()	

	def is_reservoir_attached(self):
		if self.check(): 
			return True 
		else:
			raise ReservoirError


	def attach_cap_to_barrel(self):
		return True 
