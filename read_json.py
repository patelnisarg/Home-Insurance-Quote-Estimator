import json


class JSONData:
	data_JSON = """
	{
		"CustomerID" : 1,
		"DwellingCoverage" : 100000,
		"HomeAge" : 5,
		"RoofType" : "Asphalt Shingles",
		"NumberOfUnits" : 3,
		"PartnerDiscount" : "Y"
	}
	"""

	data_dict = json.loads(data_JSON)

	customer_id = data_dict["CustomerID"]
	dwelling_coverage = data_dict["DwellingCoverage"]
	home_age = data_dict["HomeAge"]
	roof_type = data_dict["RoofType"]
	number_of_units = data_dict["NumberOfUnits"]
	partner_discount = data_dict["PartnerDiscount"]

	# print(f"Customer Id is: {customer_id}")
	# print(f"Dwelling Coverage is: {dwelling_coverage}")
	# print(f"Home Age is: {home_age}")
	# print(f"Roof Type is: {roof_type}")
	# print(f"Number of Units is: {number_of_units}")
	# print(f"Partner Discount is: {partner_discount}")
