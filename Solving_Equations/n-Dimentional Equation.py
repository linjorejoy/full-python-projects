import math


def get_value(string, unit):
    output = input("{0}({1}): ".format(string, unit))
    while True:
        try:
            output = float(output)
            return output
        except ValueError:
            print("Not a valid Number: ")
            output = get_value(string, unit)


def solutions_2n(a, b, c):
    disc = discriminant(a, b, c)
    i = 0
    if disc >= 0:
        x1 = -(b + math.sqrt(disc))/(2 * a)
        x2 = -(b - math.sqrt(disc))/(2 * a)
        return x1, x2, i, False
    else:
        print("Solutions are Imaginary")
        x1 = -b/(2 * a)
        i = math.sqrt(-disc)
        return x1, x1, i, True


def discriminant(a1, b1, c1):
    return b1 * b1 - 4 * a1 * c1


print("The equation is of the form ax^2 + bx + c = 0 ")
a = get_value("What is the value of a", "")
b = get_value("What is the value of b", "")
c = get_value("What is the value of c", "")
alpha, beta, img, imaginary = solutions_2n(a, b, c)

print("The Solutions are : ")
if imaginary:
    print("{} + i({})".format(str(alpha), img))
    print("{} - i({})".format(str(beta), img))
else:
    print("{}".format(str(alpha)))
    print("{}".format(str(beta)))
