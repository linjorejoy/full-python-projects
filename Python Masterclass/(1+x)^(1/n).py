import math

print( "*" * 50)
print("The Expansion of (1+x)^(1/n) ")
print( "*" * 50)
x = float(input("Write value of x: "))
n_ = float(input("Write the value of n: "))
iterations = int(input("Number of iterations: "))

result = 1;
e2 =1
n = 1/n_
# elements = []

for i in range(1, iterations):
    element = (x ** i)
    for j in range(i):
        e2 *= (n-j)
    element *= e2
    element /= math.factorial(i)
    elements = element
    result += element
    e2 = 1

print(result)
# print(elements)