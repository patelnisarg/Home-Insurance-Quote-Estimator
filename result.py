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

jd = JsonData(data_JSON)

c = Customer(jd)
c.calculate()
eval = Evaluation(c)

print(eval.calculate_premium())
