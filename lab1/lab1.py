from sys import argv as py_arguments
from os.path import exists as path_exists
import colorama as clrm


def get_float(message):
    try:
        result = float(input(f"{message}{clrm.Style.BRIGHT}{clrm.Fore.GREEN}"))
        print(clrm.Style.RESET_ALL, end="")
        return result
    except:
        print(
            f"{clrm.Style.RESET_ALL}{clrm.Fore.RED}",
            f"Invalid floating point number. Try again.{clrm.Style.RESET_ALL}",
        )
        return get_float(message)


def g_coef(num):
    return f"({num})" if num != 1 else ""


def print_quadratic(a, b, c):
    if a != 0:
        print(f"\nYour quadratic is {g_coef(a)}x**2 + {g_coef(b)}x + ({c}) == 0")
    else:
        print("\nThis isn`t quadratic", end="")
        print(", this is linear" if b != 0 else ", and isn`t even linear")


def solve_quadratic(a, b, c):
    if a == 0:
        return None
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
        path_to_coefs = str(py_arguments[1])
        if path_exists(path_to_coefs):
            from re import match

            in_txt = open(path_to_coefs, "r+").read()
            if match("-?\d(\.\d*)? -?\d(\.\d*)? -?\d(\.\d*)?\n", in_txt):
                value_list = in_txt[:-1].split(" ")
                a = float(value_list[0])
                b = float(value_list[1])
                c = float(value_list[2])
            else:
                print("Invalid input file format\n")
        else:
            print("Invalid path, entering interactive mode")
    except IndexError:  # there is no path argument
        a = get_float("Enter a\t")
        b = get_float("Enter b\t")
        c = get_float("Enter c\t")

    print_quadratic(a, b, c)
    print_quadratic_solution(solve_quadratic(a, b, c))
