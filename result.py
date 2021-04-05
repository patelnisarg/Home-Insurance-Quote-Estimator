from customer import Customer
from evaluation import Evaluation
from read_json import JsonData

data_JSON = {
	"CustomerID": 1,
	"DwellingCoverage": 100000,
	"HomeAge": 5,
	"RoofType": "Asphalt Shingles",
	"NumberOfUnits": 3,
	"PartnerDiscount": "Y",
}

# Passing JSON data to be parsed to string values
jd = JsonData(data_JSON)

# Creating a Customer Object to perform evaluation
c = Customer(jd)
c.calculate()

# Calculating the Premium Amount
eval = Evaluation(c)

# Output
print(f'The Final Quoted Premium Amount is: {eval.calculate_premium()}')
