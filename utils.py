from bisect import bisect_left


class Interpolate:
    def __init__(self, x_list, y_list):
        x_list = self.x_list = list(map(float, x_list))
        y_list = self.y_list = list(map(float, y_list))
        intervals = zip(x_list, x_list[1:], y_list, y_list[1:])
        self.slopes = [(y2 - y1) / (x2 - x1) for x1, x2, y1, y2 in intervals]

    def __getitem__(self, x):
        if x <= self.x_list[0]:
            return self.y_list[0]
        elif x >= self.x_list[-1]:
            return self.y_list[-1]
        else:
            i = bisect_left(self.x_list, x) - 1
            return self.y_list[i] + self.slopes[i] * (x - self.x_list[i])


class Calculations:

    @staticmethod
    def number_of_years_rating_factor(home_age: int) -> float:
        """

        :param home_age: House Age
        :return: Rating Factor related to the House Age
        """
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

    @staticmethod
    def roof_type_rating_factor(roof_type: str) -> float:
        """

        :param roof_type: Type of the Roof
        :return: Rating Factor related to the type of the roof
        """
        roof_types = {"Asphalt Shingles": 1.00, "Tin": 1.70, "Wood": 2.00}
        return roof_types[roof_type]

    @staticmethod
    def number_of_units_rating_factor(unit_num: int) -> float:
        """

        :param unit_num: Number of Units
        :return: Rating Factor related to the number of units
        """
        num_units = {1: 1.00, 2: 0.80, 3: 0.80, 4: 0.80}
        return num_units[unit_num]

    @staticmethod
    def is_discount_given(partner_discount: str) -> bool:
        """

        :param partner_discount: Y if discount is given, N if discount is not offered
        :return: bool value True if discount offered, False if not
        """
        if partner_discount == "Y":
            return True
        else:
            return False
