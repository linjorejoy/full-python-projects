d='y'
while d=='y':
    x= input(" number : ")
    for i in range(2,x):
        if x%i==0:
            print "not prime"
            break
    else :
        print "prime "
    d= raw_input ("do you want to continue y/n ")
        

        
