largest = -1000
smallest = 1000
num = 0
num = input("Enter a number: ")
smallest = num
largest = num

while True:
    num = input("Enter a number: ")

    if(num == 'done'):
        break
    elif(isinstance(num,int) or isinstance(num,int)):
        if int(num) < smallest:
            smallest = num
        if(num > largest):
            largest = num
    else:
        print("invalid")

print("Maximum is ", largest)
print("Minimum is ", smallest)
