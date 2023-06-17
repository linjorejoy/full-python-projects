
d='y'
while d=='y':
    m=input ("what is your mark : ")
    if m>=90 and m<=100:
        print "your grade is A"
    elif m>=80 and m<90:
        print "your grade is B"
    elif m>=70 and m<80:
        print "your grade is C"
    elif m>=60 and m<70:
        print "your grade is D"
    elif m>=50 and m<60:
        print "your grade is P"
    elif m>100 or m<0:
        print "-----------invalid------------"
    else :
        print " you failed nigga "
    d= raw_input("do you want to continue y/n ")
