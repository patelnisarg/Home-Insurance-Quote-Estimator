from bisect import bisect_left

class Interpolate(object):
    def __init__(self, x_list, y_list):
        if any(y - x <= 0 for x, y in zip(x_list, x_list[1:])):
            raise ValueError("x_list must be in strictly ascending order!")
        x_list = self.x_list = list(map(float, x_list))
        y_list = self.y_list = list(map(float, y_list))
        intervals = zip(x_list, x_list[1:], y_list, y_list[1:])
        self.slopes = [(y2 - y1)/(x2 - x1) for x1, x2, y1, y2 in intervals]

    def __getitem__(self, x):
        i = bisect_left(self.x_list, x) - 1
        return self.y_list[i] + self.slopes[i] * (x - self.x_list[i])


i = Interpolate([100000,150000,200000,250000,300000,350000], [0.971,1.104,1.314,1.471,1.579,1.761])
# Get the interpolated value at x = 4:
y = i[280000]
print(round(y, 3))