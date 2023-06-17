r='y'
while r=='y':
    n= int(input("enter the number : "))
    if (n>1):
        for i in range(2,n):
            if (n%i==0):
                print ( " its not prime ")
                print (i, "times " , n/i, "is ",n)
                break
        else:
            print ("its prime ")
    else :
        print (" its not even positive, how can it be prime")
    r=input ("do you want to continue : ")
