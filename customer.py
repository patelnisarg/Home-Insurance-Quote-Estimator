def number_of_years_rating_factor(home_age: int) -> float:
	num_of_years_rating_factor_value = None
	if 0 <= home_age <= 10:
		num_of_years_rating_factor_value = 1.00
	elif 11 <= home_age <= 35:
		num_of_years_rating_factor_value = 1.50
	elif 36 <= home_age <= 100:
		num_of_years_rating_factor_value = 1.80
	elif home_age > 100:
		num_of_years_rating_factor_value = 1.95
	return num_of_years_rating_factor_value


def roof_type_rating_factor(roof_type: str) -> float:
	roof_types = {"Asphalt Shingles": 1.00, "Tin": 1.70, "Wood": 2.00}
	return roof_types[roof_type]


def number_of_units_rating_factor(unit_num: int) -> float:
	num_units = {1: 1.00, 2: 0.80, 3: 0.80, 4: 0.80}
	return num_units[unit_num]


def is_discount_given(partner_discount: str) -> bool:
	if partner_discount == "Y":
		return True
	else:
		return False


class Customer:
	customer_id = None
	dwelling_coverage = None
	home_age = None
	roof_type = None
	number_of_units = None
	partner_discount = None

	def __init__(self, _data):
		self.customer_id = _data.customer_id
		self.dwelling_coverage = _data.dwelling_coverage
		self.home_age = _data.home_age
		self.roof_type = _data.roof_type
		self.number_of_units = _data.number_of_units
		self.partner_discount = _data.partner_discount

	home_age_rating_factor_value = None
	roof_type_rating_factor_value = None
	num_of_unit_factor_value = None
	discount_offered = None

	def calculate(self):
		self.home_age_rating_factor_value = number_of_years_rating_factor(self.home_age)
		self.roof_type_rating_factor_value = roof_type_rating_factor(self.roof_type)
		self.num_of_unit_factor_value = number_of_units_rating_factor(self.number_of_units)
		self.discount_offered = is_discount_given(self.partner_discount)
