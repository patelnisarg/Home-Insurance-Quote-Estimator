from read_json import JSONData as jd
import models
import utils


class Evaluation:

	@staticmethod
	def calculate_premium() -> float:
		base_premium = models.BasePremium.Base_Premium.value
		home_age_rating_factor = utils.number_of_years_rating_factor(jd.home_age)
		roof_type_rating_factor = utils.roof_type_rating_factor(jd.roof_type)
		num_of_unit_factor = utils.number_of_units_rating_factor(jd.number_of_units)
		discount_offered = utils.is_discount_given(jd.partner_discount)
		discount = 0.05
		monthly_premium = (base_premium * 0.971 * home_age_rating_factor * roof_type_rating_factor * num_of_unit_factor)

		if discount_offered:
			discount_amount = monthly_premium * discount
			monthly_premium_with_discount = monthly_premium - discount_amount
			return round(monthly_premium_with_discount)
		else:
			return round(monthly_premium)


print(Evaluation.calculate_premium())
