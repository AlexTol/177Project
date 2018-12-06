import re
from classes.constraint import Constraint
from classes.tableau import Tableau


def simplex(tab):
    while(tab.hasNegInC()):
        
        col = 0
        mostNeg = 0
        #get most negative column
        for i in range(0, len(tab.objective)):
            if(mostNeg > tab.objective[i]):
                col = i
                mostNeg = tab.objective[i]

        ratio = -1
        row = 0
        #get least positive ratio
        for i in range(0, len(tab.constraints)):
            con = tab.constraints[i]

            if(con.coefficients[col] < 0):
                continue

            if(ratio == -1):
                if(con.coefficients[col] > 0):
                    ratio = con.right/con.coefficients[col]
                row = i
            elif(con.coefficients[col] == 0):
                continue
            elif(con.right/con.coefficients[col] < ratio):
                ratio = con.right/con.coefficients[col]
                row = i
            #print(row)
            #print(i)
            #print(con.right)
            #print(con.coefficients[col])
            #print(ratio)
            #print(con.right/con.coefficients[col])

        print('pivotring at ' + str(row) +',' + str(col))
        tab.pivot(row,col)
            




constraints = []

c1 = Constraint()
vals = []
for i in range (0,60):
    if(i < 30):
        vals.append(1)
    else:
        vals.append(0)
c1.setConstraint(vals,'<=',150000)

c2 = Constraint()
vals = []
for i in range (0,60):
    if(i < 30):
        vals.append(0)
    else:
        vals.append(1)
c2.setConstraint(vals,'<=',200000)

c3 = Constraint()
vals = []
for i in range (0,60):
    if(i >= 6 and i < 12):
        vals.append(1)
    elif(i >= 36 and i < 42):
        vals.append(1)
    else:
        vals.append(0)
c3.setConstraint(vals,'<=',70000)

c4 = Constraint()
vals = []
for i in range (0,60):
    if(i >= 12 and i < 18):
        vals.append(1)
    elif(i >= 42 and i < 48):
        vals.append(1)
    else:
        vals.append(0)
c4.setConstraint(vals,'<=',50000)

c5 = Constraint()
vals = []
for i in range (0,60):
    if(i >= 18 and i < 24):
        vals.append(1)
    elif(i >= 48 and i < 54):
        vals.append(1)
    else:
        vals.append(0)
c5.setConstraint(vals,'<=',100000)

c6 = Constraint()
vals = []
for i in range (0,60):
    if(i >= 24 and i < 30):
        vals.append(1)
    elif(i >= 54 and i < 60):
        vals.append(1)
    else:
        vals.append(0)
c6.setConstraint(vals,'<=',40000)


c7 = Constraint()
vals = []
locs = [0,6,12,18,24,30,36,42,48,54]
for i in range(0,60):
    if i in locs:
        vals.append(1)
    else:
        vals.append(0)
c7.setConstraint(vals,'=',50000)

c8 = Constraint()
vals = []
locs = [1,7,13,19,25,31,37,43,49,55]
for i in range(0,60):
    if i in locs:
        vals.append(1)
    else:
        vals.append(0)
c8.setConstraint(vals,'=',10000)

c9 = Constraint()
vals = []
locs = [2,8,14,20,26,32,38,44,50,56]
for i in range(0,60):
    if i in locs:
        vals.append(1)
    else:
        vals.append(0)
c9.setConstraint(vals,'=',40000)

c10 = Constraint()
vals = []
locs = [3,9,15,21,27,33,39,45,51,57]
for i in range(0,60):
    if i in locs:
        vals.append(1)
    else:
        vals.append(0)
c10.setConstraint(vals,'=',35000)

c11 = Constraint()
vals = []
locs = [4,10,16,22,28,34,40,46,52,58]
for i in range(0,60):
    if i in locs:
        vals.append(1)
    else:
        vals.append(0)
c11.setConstraint(vals,'=',60000)

c12 = Constraint()
vals = []
locs = [5,11,17,23,29,35,41,47,53,59]
for i in range(0,60):
    if i in locs:
        vals.append(1)
    else:
        vals.append(0)
c12.setConstraint(vals,'=',20000)

constraints.append(c1)
constraints.append(c2)
constraints.append(c3)
constraints.append(c4)
constraints.append(c5)
constraints.append(c6)
constraints.append(c7)
constraints.append(c8)
constraints.append(c9)
constraints.append(c10)
constraints.append(c11)
constraints.append(c12)

f = open('obj.txt')
line = f.readline()
line = line.rstrip()
obj = []
for num in line.split(' '):
    obj.append(int(num))

t = Tableau()
t.setTableau(constraints,obj)

t.normalize()
t.objToNeg()
print(' ')
print('INITIAL TABLEAU')
for con in t.constraints:
    print(con.coefficients)
    print(con.right)
print(t.objective)

simplex(t)
print(' ')
print('FINAL TABLEAU')
for con in t.constraints:
    print(con.coefficients)
    print(con.right)
print(t.objective)
print(t.objVal)


print('\n\n\n FINAL answer')
print(t.getAnswers())

