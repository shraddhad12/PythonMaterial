def mean_tuple(numbers):
    result = [sum(x) / len(x) for x in numbers]
    return result
print(mean_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))


class Circle:
    def __init__(self):
        self.radius = 5

    @staticmethod
    def area():
        return 3.14

circle1 = Circle()
print(circle1.area())