# import numpy as np
import math
AVAILABLE_MODULES_RECOMMENDED = [1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 32, 40, 50]
# AVAILABLE_MODULES_CHOICE2 = [1.125, 1.375, 1.75, 2.25, 2.75, 3.5, 4.5, 5.5, 7, 9, 11, 14, 18, 22, 28, 36, 45]
# AVAILABLE_MODULES_CHOICE3 = [3.25, 3.75, 6.5]


def standardise(array, key):
    for i in range(len(array)):
        if array[i] > key:
            return array[i]
    return 0


def check_statement(string):
    print("If true type 1 otherwise type 0: ")
    while True:
        check = input("{}".format(string))
        if check == '0':
            return False
        elif check == '1':
            return True
        else:
            continue


def get_value(string, unit):
    output = input("{0}({1}): ".format(string, unit))
    while True:
        try:
            output = float(output)
            return output
        except ValueError:
            print("Not a valid Number: ")
            output = get_value(string, unit)


def material_selection():
    if check_statement("Is the material given: "):
        sigma_d1 = get_value("What is the value of sigma(d) for pinion", "N/mm2")
        sigma_d2 = get_value("What is the value of sigma(d) for gear", "N/mm2")
        return sigma_d1, sigma_d2
    else:
        print("Take a suitable material from DataBook page 463 or page 473: ")
        sigma_d = get_value("What is the value of sigma(d): ", "N/mm2")
        return sigma_d, sigma_d


def lewis_form_factor(z):
    if check_statement("is it involute"):
        if check_statement("pressure angle is 14.5 deg "):
            return 0.124 - 0.684/z
        elif check_statement("pressure angle is 20 deg "):
            return 0.154 - 0.912/z
        else:
            return 0.154
    elif check_statement("Does it have Stub teeth"):
        if check_statement("pressure angle is 20 deg "):
            return 0.175 - 0.912/z
        else:
            return 0.175
    else:
        return 0.154


def velocity_factor():
    if check_statement("Velocity is Given?"):
        v = get_value("What is the value of velocity?", "m/s")
        if check_statement("Ordinary cut") and v <= 8:
            return 3.05 / (3.05 + v)
        else:
            if check_statement("Carefully cut") and v <= 13:
                return 4.58 / (4.58 + v)
            else:
                if check_statement("accurately cut") and 6 <= v <= 20:
                    return 6.1 / (6.1 + v)
                else:
                    if check_statement("hardened steel? ") and v >= 20:
                        return 5.55 / (5.55 + v)
                    else:
                        if check_statement("Non-Metallic Gears"):
                            return 0.7625 / (1.0167 + v)
                        else:
                            return 0.5
    else:
        return 0.5


def weaker_part(sigma_d1, sigma_d2):
    z1 = 10
    z2 = 10

    if check_statement("Is the number of teeth of pinion given? "):
        z1 = math.floor(get_value("Number of teeth of pinion", "Integer"))
    if check_statement("Is the number of teeth of gear given? "):
        z2 = math.floor(get_value("Number of teeth of gear", "Integer"))

    y1 = lewis_form_factor(z1)
    y2 = lewis_form_factor(z2)

    # Identify the weaker part
    if sigma_d1 * y1 > sigma_d2 * y2:
        weakerpart = "gear"
        y = y2
        z = z2
        sigma_d = sigma_d2
        print("Design based on gear")
    else:
        weakerpart = "pinion"
        y = y1
        z = z1
        sigma_d = sigma_d1
        print("Design based on pinion")
    return weakerpart, sigma_d, y, z, z1, z2


def find_module(weakerpart, sigma_d, Cv, y, z):
    # Find the Module
    P = get_value("What is the power at {}".format(weakerpart), "kW")
    N = get_value("What is the rpm of {}".format(weakerpart), "rpm")
    if check_statement("Value of k = b / m given? "):
        k = get_value("What is the value of k: ", "")
    else:
        print("Assume value of k between 9.5 and 12.5")
        k = get_value("What is the value of k: ", "")

    if check_statement("Diameter of {} is known? ".format(weakerpart)):
        d = get_value("What is the value of Diameter", "mm")
        print("Finding the value of Tangential force, Ft", "N")
        Cs = get_value("What is the value of Service Factor", "")
        # velocity
        v = (math.pi * d * N) / 60
        Ft = 1000 * P * Cs / v

        m = math.sqrt(Ft/(sigma_d*Cv*k*y*math.pi))
    else:
        Mt = P * 60 / (2 * math.pi * N)
        m = math.pow((2 * Mt / (sigma_d * Cv * k * y * math.pi * z)), 1/3)
        d = m * z
        Cs = get_value("What is the value of Service Factor", "")
        # velocity
        v = (math.pi * d * N) / 60
        Ft = 1000 * P * Cs / v
    m = standardise_module(m)
    return m, Ft, d, v


def standardise_module(m):
    return standardise(AVAILABLE_MODULES_RECOMMENDED, m)


def check_for_safety(m, Ft, Cv, y, z, sigma_d):
    sigma_d_check = Ft / (Cv * y * z)
    print("Checking safety for m = {}".format(m))

    if sigma_d_check < sigma_d:
        m = standardise_module(m + 0.1)
        m = check_for_safety(m, Ft, Cv, y, z, sigma_d)
    else:
        print("Design is Safe")
    return m


def dynamic_strength(Ft, v, b):
    K3 = 20.67
    e = 0.01
    E1 = get_value("What is module of elasticity of Pinion:", "MN/m2 or N/mm2")
    E2 = get_value("What is module of elasticity of Gear:", "MN/m2 or N/mm2")

    # to find k1
    if check_statement("Is it  14.5deg full Depth Teeth"):
        k1 = 9.345
    else:
        if check_statement("Is it  20deg full Depth Teeth"):
            k1 = 9.0
        else:
            if check_statement("Is it  20deg Stub Teeth"):
                k1 = 8.70
            else:
                k1 = 9
    C = e / (k1 * ((1/E1) + (1/E2)))
    Fd = Ft + K3 * v * (C * b + Ft) / (K3 * v + math.sqrt(C * b + Ft))
    return Fd


def endurance_strength(b, Y, m):
    sigma_en = get_value("What is the value of Endurance limit from Table 12.15", "MN/m2 or N/mm2")
    Fen = sigma_en * b * Y * m
    return Fen


def check_endurance_strength(b, Y, m):
    sigma_en = get_value("What is the next value of Endurance limit from Table 12.15", "MN/m2 or N/mm2")
    Fen = sigma_en * b * Y * m
    return Fen


def wear_tooth_load(d1, d2, b, Fd):
    Q = 2 * d2 / (d1 + d2)
    K = get_value("Load Stress factor from Table 12.16 based on BHN from Table 15.15 ", "")
    Fw = d1 * b * Q * K
    if Fw > Fd:
        print("Design is safe")
    else:
        print("Increase the value of BHN")
        return wear_tooth_load(d1, d2, b, Fd)
    return Fw


def second_part_of_design(m, Ft, Cv, y, z, sigma_d, v, b):
    # CHECK FOR SAFETY 𝐅𝐭 = 𝛔𝐝 𝐂𝐯 𝐛 𝐘 𝐦
    m = check_for_safety(m, Ft, Cv, y, z, sigma_d)

    # DYNAMIC STRENGTH
    Fd = dynamic_strength(Ft, v, b)

    # ENDURANCE STRENGTH
    Fen = endurance_strength(b, y * math.pi, m)

    if Fen >= Fd:
        print('Design is Safe')
    else:
        if check_statement("can the sigma_en be increased?"):
            Fen = check_endurance_strength(b, y * math.pi, m)
        else:
            m = standardise_module(m + 0.001)
            m, Fd, Fen = second_part_of_design(m, Ft, Cv, y, z, sigma_d, v, b)

    return m, Fd, Fen


def main():
    # MATERIAL SELECTION
    sigma_d1, sigma_d2 = material_selection()

    # WEAKER PART
    weakerpart, sigma_d, y, z, z1, z2 = weaker_part(sigma_d1, sigma_d2)

    # FIND THE MODULE
    Cv = velocity_factor()
    m, Ft, d, v = find_module(weakerpart, sigma_d, Cv, y, z)
    d1 = m * z1
    d2 = m * z2

    # Find the Width
    b = get_value("What is the width", "mm")

    # SECOND PART
    m, Fd, Fen = second_part_of_design(m, Ft, Cv, y, z, sigma_d, v, b)

    # WEAR TOOTH LOAD
    Fw = wear_tooth_load(d1, d2, b, Fd)

    # DESIGN IS COMPLETE
    print("#" * 30)
    print("#" * 30)
    print("#" * 5, "DESIGN IS COMPLETE", "#" * 5)
    print("#" * 30)
    print("#" * 30)

    print("*" * 5, "DETAILS OF GEAR SET", "*" * 5)
    print("Module of Gear = {}".format(m))
    print("Gear Width = {}".format(b))

    print("*" * 5, "DETAILS OF INDIVIDUAL GEARS", "*" * 5)
    print("Details of Pinion")
    print("Number of Teeth(z1) = {}".format(z1))
    print("Diameter = {}".format(d1))
    print("𝛔𝐝 = {}".format(sigma_d1))

    print("Details of Gear")
    print("Number of Teeth(z1) = {}".format(z2))
    print("Diameter = {}".format(d2))
    print("𝛔𝐝 = {}".format(sigma_d2))

    print("*" * 5, "LOADS ACTING ON GEARS", "*" * 5)
    print("Ft = {}".format(Ft))
    print("Fd = {}".format(Fd))
    print("Fen = {}".format(Fen))
    print("Fw = {}".format(Fw))


main()
