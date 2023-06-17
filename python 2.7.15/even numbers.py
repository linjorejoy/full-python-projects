d='y'
while d=='y':
    x= input ("final number : ")
    for i in range(x+1):
        if i%2==0:
            print i
    d=raw_input("do you want to continue y/n ")
