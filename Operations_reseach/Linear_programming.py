import numpy as np

symbols = {1: "<",
           2: "<=",
           3: ">",
           4: ">=",
           5: "="}

NO_OF_EQUATIONS = 20
NO_OF_VARIABLES = 10
TABLE_ROWS = 50
TABLE_COLUMNS = 50


def get_number(number):
    while True:
        try:
            number = int(number)
            return number
        except ValueError:
            print("Not a number")
            number = get_number(input("Try again: "))
            continue


def return_symbol():
    print(symbols)
    while True:
        sym = input("Input Symbol Key: ")
        try:
            sym = int(sym)
            if 1 <= sym <= len(symbols):
                return sym
            else:
                continue
        except ValueError:
            print("Invalid Key")
            continue


def print_equation(nth_eqn):
    print("The equation is ")
    if nth_eqn is not 0:
        print(" + ".join(["{}(x{})".format(equations[nth_eqn][i], i+1)
                          for i in range(len(equations[nth_eqn]))
                          if int(equations[nth_eqn][i]) is not 0]), sep=" ", end="")

        print(" {} {}".format(symbols[symbols_array[nth_eqn]], free_term[nth_eqn][0]))
    else:
        print("Z", symbols[symbols_array[nth_eqn]], end=" ")
        print(" + ".join(["{}(x{})".format(equations[nth_eqn][i], i+1)
                          for i in range(len(equations[nth_eqn]))
                          if int(equations[nth_eqn][i]) is not 0]), sep=" ")


def input_equations(nth_eqn):
    n_variables = get_number(input("How many variables are there for equation no.{} : ".format(int(nth_eqn))))
    if nth_eqn is not 0:
        print("The equations are of the form a1(x1)+ a2(x2) + ... = N ")

        for i in range(n_variables):
            coefficient = get_number(input("What is the value of a{}: ".format(i + 1)))
            equations[nth_eqn][i] = coefficient
        sym = return_symbol()
        symbols_array.append(sym)

        free_term_of_this_equation = get_number(input("What is the value of N: "))
        free_term[nth_eqn] = free_term_of_this_equation
    else:
        print("The equations are of the form Z = a1(x1)+ a2(x2) + ...")
        for i in range(n_variables):
            coefficient = get_number(input("What is the value of a{}: ".format(i + 1)))
            equations[nth_eqn][i] = coefficient
        symbols_array.append(5)
    print_equation(nth_eqn)


def standardise_equation():
    pass


def main():
    no_of_dashes = 10
    print("Write the equation to be optimised: ")
    input_equations(0)
    n_eqn = int(get_number(input("How many constraints are there: ")))
    print("*"*no_of_dashes)
    for i in range(1, n_eqn+1):
        input_equations(i)
        print("-"*no_of_dashes)
    print("*" * no_of_dashes)


equations = np.zeros((NO_OF_EQUATIONS, NO_OF_VARIABLES), int)

symbols_array = []

free_term = np.zeros((NO_OF_EQUATIONS, 1), int)

table = np.ones((TABLE_ROWS, TABLE_COLUMNS), int)
num_array = []
main()
