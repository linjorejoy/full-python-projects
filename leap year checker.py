
r='y'
while r=='y':
    year = input ("enter the year")
    if (int(year) % 4) == 0:
       if (int(year) % 100) == 0:
           if (int(year) % 400) == 0:
               print( year + " is a leap year")
           else:
               print(year + " is not leap year")
       else:
           print(year + " is a leap year")
    else:
       print(year + " is not a leap year")
    r=input("do you want to continue y/n ")

