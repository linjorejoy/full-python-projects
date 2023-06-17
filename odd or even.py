
r='y'


while r=='y':
    n = int(input("Enter a number to find fact : "))
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    print (fact)
    r= input("do you want to continue y/n ")
        
     
