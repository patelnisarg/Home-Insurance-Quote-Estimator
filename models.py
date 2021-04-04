from enum import Enum


class RoofType(Enum):
	Asphalt_Shingles = 1.00
	Tin = 1.70
	Wood = 2.00


class BasePremium(Enum):
	Base_Premium = 350


class NumOfUnits(Enum):
	One = 1.00
	Two = 0.80
	Three = 0.80
	Four = 0.80
