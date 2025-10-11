from src.calculator import Calculator
from src.constants import USER_WELCOME_MESSAGE, USER_GOODBYE_MESSAGE


def main():
    calc = Calculator()
    print(USER_WELCOME_MESSAGE)
    while True:
        try:
            expr = input("Insert your expression: ")
        except KeyboardInterrupt:
            print("\n", USER_GOODBYE_MESSAGE)
            break
        if expr == "exit":
            print(USER_GOODBYE_MESSAGE)
            break

        try:
            result = calc.calculate_rpn(expr)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
