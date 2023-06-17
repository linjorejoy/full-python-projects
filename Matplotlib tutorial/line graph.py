import matplotlib.pyplot as plt

with open("G:\my works new\Python\Matplotlib tutorial\original.txt","r") as f:
    htg = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    atg = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
#print (htg)
#print (atg)           


xVar = []
for i in range(len(htg)):
    xVar.append(i)

    
plt.scatter(xVar,htg, c= "green",s=2)
plt.title(r"HomeTeamGoals $ ^(sin(x))$")


plt.xlim(-10,150)
plt.xlabel("x")
plt.xticks([25,50,75],["2__5","5__0","7__5"])

plt.ylim(-2,10)
plt.ylabel("y")
plt.yticks([1,3,6],[1,"three","six"])

plt.savefig("G:\my works new\Python\Matplotlib tutorial\linegraph.pdf")
plt.show()


