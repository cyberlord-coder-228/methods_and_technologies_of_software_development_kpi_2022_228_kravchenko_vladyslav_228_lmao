from sys import argv as arguments
from os.path import exists as path_exists


def g_coef(num):
    if num == 1:
        return ""
    elif num < 0:
        return f"({num})"
    else:
        return str(num)


def print_quadratic(a, b, c):
    if a != 0:
        print(f"\nYour quadratic is {g_coef(a)}x**2 + {g_coef(b)}x + ({c}) == 0")
    else:
        print("\nThis is not quadratic")
        if b != 0:
            print("...this is linear")
        else:
            print("...and isn`t even linear")


def solve_quadratic(a, b, c):
    if a == 0:
        return
    else:
        from math import sqrt

        try:
            result = set()
            discriminant = sqrt(b**2 - 4 * a * c)
        except ValueError:
            pass
        else:
            result.add((-b + discriminant) / 2 * a)
            result.add((-b - discriminant) / 2 * a)
        finally:
            return result


def print_quadratic_solution(solution_set):
    if solution_set is None:
        pass
    elif len(solution_set) == 0:
        print("\nRoots to quadratic are not real")
    elif len(solution_set) == 1:
        print("\nThe roots coincide,")
        print(f"x = {next(iter(solution_set))} is a solution")
    else:
        print("\nTwo real roots found")
        for root in solution_set:
            print(f"{root} is a solution")


if __name__ == "__main__":
    print("\nThis program solves quadratic equations (ax**2 + bx + c)")

    try:
        path_to_vars = str(arguments[1])
        if path_exists(path_to_vars):
            from re import match

            in_txt = open(path_to_vars, "r+").read()
            if match("-?\d(\.\d*)?\s-?\d(\.\d*)?\s-?\d(\.\d*)?\n", in_txt):
                value_list = in_txt[:-1].split(" ")
                a = float(value_list[0])
                b = float(value_list[1])
                c = float(value_list[2])
            else:
                print("Invalid input file format\n")
        else:
            print("Invalid path")
    except:
        a = float(input("Enter a\t"))
        b = float(input("Enter b\t"))
        c = float(input("Enter c\t"))

    print_quadratic(a, b, c)
    print_quadratic_solution(solve_quadratic(a, b, c))
