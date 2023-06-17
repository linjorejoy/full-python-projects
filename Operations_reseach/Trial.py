import OperationsResearch as OR

newTable = [
    [1,2,3,4],
    [4,3,2,1],
    [4,5,6,7],
    [5,10,12,15]
]
opRes = OR.AssignmentProblem(newTable)


print(opRes.RowReduced())
print(opRes.ColumnReduced())