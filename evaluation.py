import models


class Evaluation:

	home_age_rating_factor_value = None
	dwelling_coverage_rating_factor_value = None
	roof_type_rating_factor_value = None
	num_of_unit_factor_value = None
	discount_offered = None

	def __init__(self, customer_data):
		self.customer_id = customer_data.customer_id
		self.dwelling_coverage_rating_factor_value = customer_data.dwelling_coverage_rating_factor_value
		self.home_age_rating_factor_value = customer_data.home_age_rating_factor_value
		self.roof_type_rating_factor_value = customer_data.roof_type_rating_factor_value
		self.num_of_unit_factor_value = customer_data.num_of_unit_factor_value
		self.discount_offered = customer_data.discount_offered

	def calculate_premium(self) -> float:
		base_premium = models.BasePremium.Base_Premium.value
		home_age_rating_factor = self.home_age_rating_factor_value
		dwelling_coverage = self.dwelling_coverage_rating_factor_value
		roof_type_rating_factor = self.roof_type_rating_factor_value
		num_of_unit_factor = self.num_of_unit_factor_value
		discount_offered = self.discount_offered
		discount = models.BaseDiscount.Base_Discount.value

		monthly_premium = (
					base_premium * dwelling_coverage * home_age_rating_factor * roof_type_rating_factor * num_of_unit_factor)

		if discount_offered:
			discount_amount = monthly_premium * discount
			monthly_premium_with_discount = monthly_premium - discount_amount
			return round(monthly_premium_with_discount)
		else:
			return round(monthly_premium)
