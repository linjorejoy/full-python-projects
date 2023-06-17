dividant = float(input("Enter the dividant: "))
divisor = float(input("Enter the divisor: "))
print(dividant/divisor)
n = int(input("How many decimal places do you need: "))
quotient = []
print(len(str(int(dividant/divisor))))

for i in range(n):
    quo = int(dividant/divisor)
    if i == 1:
        quotient.append(".")
    quotient.append(quo)
    sub = quo*divisor
    rem = dividant - sub
    dividant = 10 * rem

print(quotient)