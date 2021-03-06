import re
from .constraint import Constraint

class Tableau(object):

    def __init__(self):
        self.constraints = []
        self.objective = []
        self.columns = []
        self.objVal = 0
        self.originalC = 0

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
        self.originalC = len(self.constraints[0].coefficients)

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
            if(i in alreadyNormal or self.constraints[i].equality == '='):
                continue
            else:
                for j in range(0, len(self.constraints)):
                    if(j == i):
                        self.constraints[j].coefficients.append(1)
                    else:
                        self.constraints[j].coefficients.append(0)
                self.objective.append(0)

        self.resetColumns()

    def objToNeg(self):
        for i in range(0,len(self.objective)):
            self.objective[i] = self.objective[i] * -1

        self.resetColumns()

    def hasNegInC(self):
        for val in self.objective:
            if(int(val) < 0):
                return True
            
        return False
    
    def pivot(self, row, column):
        val = self.constraints[row].coefficients[column]
        #print('val ' + str(val))

        for i in range(0,len(self.constraints[row].coefficients)):
            self.constraints[row].coefficients[i] = self.constraints[row].coefficients[i]/val
        self.constraints[row].right = self.constraints[row].right/val
        
        for i in range(0,len(self.constraints)):
            if( i == row):
                continue
            val2 = self.constraints[i].coefficients[column]
            #print('val2 ' + str(val2))

            for j in range(0,len(self.constraints[i].coefficients)):
                self.constraints[i].coefficients[j] = self.constraints[i].coefficients[j] - (val2 * self.constraints[row].coefficients[j])
            self.constraints[i].right = self.constraints[i].right - (val2 * self.constraints[row].right)

        val3 = self.objective[column]
        for i in range(0,len(self.objective)):
            self.objective[i] = self.objective[i] - (val3 * self.constraints[row].coefficients[i])

        self.objVal = self.objVal - (val3 * self.constraints[row].right)
        self.resetColumns()

    def getAnswers(self):
        answers = []
        aNRegex = '0*10*\Z'
            
        for i in range(0, self.originalC):
            string = ''
            for num in self.columns[i]:
                string = string + str(int(num))
            string = string + str(int(self.objective[i]))
            #print(string)

            loc = 0
            for j in range(0,len(string) - 1):
                if(string[j] == '1'):
                    break
                loc = j

            if(re.match(aNRegex,string)):
                answers.append(int(self.constraints[loc].right))
            else:
                answers.append(0)
        
        return answers
        
