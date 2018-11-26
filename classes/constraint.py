class Constraint(object):


    def __init__(self):
        self.normalForm = False
        self.coefficients = []
        self.equality = '<='
        self.right = 0

    def setConstraint(self,vals, eq, r, normal = False):
        for val in vals:
            self.coefficients.append(val)

        self.equality = eq
        self.right = r
        self.normalForm =  normal

    def mult(self,val):
        for i in range(0,len(self.coefficients)):
            self.coefficients[i] = self.coefficients[i] * val

    