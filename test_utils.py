from unittest import TestCase

from utils import *


class TestCalculations(TestCase):
	def test_number_of_years_rating_factor(self):
		home_age = 77
		expected_value = Calculations.number_of_years_rating_factor(home_age)
		self.assertEqual(expected_value, 1.80)

	def test_roof_type_rating_factor(self):
		roof_type = "Asphalt Shingles"
		expected_value = Calculations.roof_type_rating_factor(roof_type)
		self.assertEqual(expected_value, 1.00)

	def test_number_of_units_rating_factor(self):
		unit_num = 2
		expected_value = Calculations.number_of_units_rating_factor(unit_num)
		self.assertEqual(expected_value, 0.80)

	def test_is_discount_given(self):
		partner_discount = "N"
		expected_value = Calculations.is_discount_given(partner_discount)
		self.assertFalse(expected_value)
