from utils import Calculations as cal

from utils import Interpolate


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
		self.i = Interpolate([100000, 150000, 200000, 250000, 300000, 350000],
		                     [0.971, 1.104, 1.314, 1.471, 1.579, 1.761])

	home_age_rating_factor_value = None
	dwelling_coverage_rating_factor_value = None
	roof_type_rating_factor_value = None
	num_of_unit_factor_value = None
	discount_offered = None

	def calculate(self):
		self.home_age_rating_factor_value = cal.number_of_years_rating_factor(self.home_age)
		self.dwelling_coverage_rating_factor_value = self.i[self.dwelling_coverage]
		self.roof_type_rating_factor_value = cal.roof_type_rating_factor(self.roof_type)
		self.num_of_unit_factor_value = cal.number_of_units_rating_factor(self.number_of_units)
		self.discount_offered = cal.is_discount_given(self.partner_discount)
