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
	roof_type_rating_factor_value = None
	if roof_type == "Asphalt Shingles":
		roof_type_rating_factor_value = 1.00
	elif roof_type == "Tin":
		roof_type_rating_factor_value = 1.70
	elif roof_type == "Wood":
		roof_type_rating_factor_value = 2.00
	return roof_type_rating_factor_value


def number_of_units_rating_factor(unit_num: int) -> float:
	number_of_units_rating_factor_value = None
	if unit_num == 1:
		number_of_units_rating_factor_value = 1.00
	elif unit_num == 2:
		number_of_units_rating_factor_value = 0.80
	elif unit_num == 3:
		number_of_units_rating_factor_value = 0.80
	elif unit_num == 4:
		number_of_units_rating_factor_value = 0.80
	return number_of_units_rating_factor_value


def is_discount_given(partner_discount: str) -> bool:
	if partner_discount == "Y":
		return True
	else:
		return False
