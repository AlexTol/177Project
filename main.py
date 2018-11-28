import re
from classes.constraint import Constraint
from classes.tableau import Tableau


def simplex(tab):
    while(tab.hasNegInC()):
        print('why are we still here?')


c1 = Constraint()
c1.setConstraint([1,2,3],'<=',10)

c2 = Constraint()
c2.setConstraint([4,5,6],'<=',20)

c3 = Constraint()
c3.setConstraint([7,8,9],'<=',30)

obj = [10,11,12]
t = Tableau()
t.setTableau([c1,c2,c3],obj)

print(t.objective)
print(t.hasNegInC())
t.objToNeg()
print(t.objective)
print(t.hasNegInC())

for con in t.constraints:
    print(con.coefficients)

print(' ')

for col in t.columns:
    print(col)

print(' ')
t.normalize()

for con in t.constraints:
    print(con.coefficients)

print(' ')

for col in t.columns:
    print(col)

print(' ')
t.pivot(0,0)

for con in t.constraints:
    print(con.coefficients)
    print(con.right)


print(' ')

print(t.objective)
print(' ')
print('objVal ' + str(t.objVal))

print(' ')


