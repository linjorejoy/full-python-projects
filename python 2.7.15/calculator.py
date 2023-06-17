def add(a,b):
    return a+b
def subt(a,b):
    return a-b
def divi (a,b):
    return a/b
def mult (a,b):
    return a*b
print "what do you want to do"
x=input (" 1.add \n 2.subtract \n 3.divi \n 4.multiply \n")
c= input ("first number : ")
d= input ("second number : ")

if x==1:
    print add(c,d)
elif x==2:
    print subt(c,d)
elif x==3:
    print divi(float(c),d)
elif x==4:
    print mult(c,d)
else :
    print "not an option"
    
