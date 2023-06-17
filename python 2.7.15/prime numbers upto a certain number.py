a= input ("final number : ")
flag=0
for i in range (2,a):
    for j in range(2,i):
        if i%j==0:
            flag=flag+1

    if flag ==0:
        print i
    flag=0
