class Polynomial:
    pass

p1 = Polynomial()
p2 = Polynomial()
p1.coeffs = 1, 2, 3 # x^2 + 2x + 3
p2.coeffs = 3, 4, 3 # 3x^2 + 4x + 3

class Polynomial1:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial1(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial1(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)
    
    def __call__(self):
        pass

p3 = Polynomial1(1, 2, 3)
p4 = Polynomial1(3, 4, 3)