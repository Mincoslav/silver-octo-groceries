import numbers


class FoodItem:
	def __init__(self, name: str, price: float):
		self.name = name
		self.price = price


class Vegetable(FoodItem):
	tag = 'vegetable'

	def __init__(self, name, price, weight: [float, str], country_of_origin):
		super().__init__(name, price)
		self.weight = weight
		self.price_per_kg = self.calculate_price_per_kg()
		self.country_of_origin = country_of_origin

	def calculate_price_per_kg(self):
		if self.weight[1] in ['kg']:
			return self.price / self.weight[0]
		elif self.weight[1] in ['g', 'gram', 'grams']:
			return self.price / self.weight[0] * 1000
