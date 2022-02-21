def print_quadratic(a, b, c):
    if a != 0:
        print(f"\nYour quadratic is {a}x**2 + ({b}x) + ({c}) == 0")
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
    print("\nThis program solves quadratic equations\n(ax**2 + bx + c)\n")

    a = int(input("Enter a\t"))
    b = int(input("Enter b\t"))
    c = int(input("Enter c\t"))

    print_quadratic(a, b, c)
    print_quadratic_solution(solve_quadratic(a, b, c))
