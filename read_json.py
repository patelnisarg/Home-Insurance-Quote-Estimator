class JsonData:
	"""
	Parse JSON Data to String
	"""
	customer_id = None
	dwelling_coverage = None
	home_age = None
	roof_type = None
	number_of_units = None
	partner_discount = None

	def __init__(self, custom_dict):
		self.customer_id = custom_dict["CustomerID"]
		self.dwelling_coverage = custom_dict["DwellingCoverage"]
		self.home_age = custom_dict["HomeAge"]
		self.roof_type = custom_dict["RoofType"]
		self.number_of_units = custom_dict["NumberOfUnits"]
		self.partner_discount = custom_dict["PartnerDiscount"]

