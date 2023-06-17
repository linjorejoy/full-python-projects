from math import inf
import numpy as np

class operations_research:

    def __init__(self):
        pass


class TableTypeProblems(operations_research):
    def __init__(self,TABLE):
        self.TABLE = TABLE
    
    def RowReduced(self):
        for i in range(len(self.TABLE)):
            min = inf
            for j in range(len(self.TABLE[i])):
                if(self.TABLE[i][j] < min ):
                    min = self.TABLE[i][j]
            for j in range(len(self.TABLE[i])):
                self.TABLE[i][j] -= min
        return self.TABLE

    def ColumnReduced(self):
        for j in range(len(self.TABLE[0])):
            min = inf
            for i in range(len(self.TABLE)):
                if(self.TABLE[i][j] < min ):
                    min = self.TABLE[i][j]
            for i in range(len(self.TABLE)):
                self.TABLE[i][j] -= min
        return self.TABLE

    def isZeroInArray(self,array):
        for i in range(len(array)):
            if(array[i] == 0):
                return True
        return False

    # This function finds out the number of zeroes in a given array
    def NumOfZeroInArray(self,array):
        count = 0
        for i in range(len(array)):
            if(array[i] == 0):
                count +=1
        return count


class AssignmentProblem(TableTypeProblems):
    def __init__(self,TABLE):
        self.TABLE = TABLE
    
    def isBalanced(self):
        return len(self.TABLE) == len(self.TABLE[0])
    
    
    # This is to cross out all elements in a column(colNum) of an array. colNum(0-n)
    def ColumnCheck(self,array,colNum):
        pass
    
    # This is to cross out all the elements in a row(rowNum) of an array. rowNum(0-n)
    def RowCheck(self,array,rowNum):
        pass
    
    # This is to find out the number of lines required to cross out all the zeroes
    def NumberOfLinesRequired(self):
        checkArray = np.zeros((len(self.TABLE), len(self.TABLE[0])), dtype=int )

        # Rows Scanning
        for i in range(len(self.TABLE)):
            if(self.NumOfZeroInArray(self.TABLE[i]) > 0 ):
                pass

        # Column Scanning