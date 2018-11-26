import re
from .constraint import Constraint

class Tableau(object):

    def __init__(self):
        self.constraints = []
        self.objective = []
        self.columns = []

    def setTableau(self,cons, obj):
        for con in cons:
            self.constraints.append(con)
        for val in obj:
            self.objective.append(val)

        for con in self.constraints:
            i = 0
            for val in con.coefficients:
                try:
                    self.columns[i].append(val)
                except:
                     self.columns.append([])
                     self.columns[i].append(val)
                i += 1

    def resetColumns(self):
        self.columns = []
        for con in self.constraints:
            i = 0
            for val in con.coefficients:
                try:
                    self.columns[i].append(val)
                except:
                     self.columns.append([])
                     self.columns[i].append(val)
                i += 1
                


    def normalize(self):
        alreadyNormal = []
        aNRegex = '0*10*\Z'

        for i in range(0, len(self.constraints)):
            string = ''
            for col in self.columns:
                string = string + str(col[i])
            string = string + str(self.objective[i])

            if(re.match(aNRegex,string)):
                alreadyNormal.append(i)

        for i in range(0, len(self.constraints)):
            if(i in alreadyNormal):
                continue
            else:
                for j in range(0, len(self.constraints)):
                    if(j == i):
                        self.constraints[j].coefficients.append(1)
                    else:
                        self.constraints[j].coefficients.append(0)
                self.objective.append(0)

        self.resetColumns()
        
            
