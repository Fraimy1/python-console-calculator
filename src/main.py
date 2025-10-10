from calculator import Calculator

user_welcome_message = """
=============================================
Welcome to the RPN calculator!
You can insert any RPN expression and the calculator will return the result.
e.g. "6 2 +" -> 8 or something crazy like "( 3 (4        (2)   -) ** )" 
it can handle it (probably)
Press Ctrl + C or type in "exit" to exit
=============================================
"""

if __name__ == '__main__':
    calc = Calculator()
    print(user_welcome_message)
    while True:
        expr = input("Insert your expression: ")
        if expr == "exit":
            break
        try: 
            result = calc.calculate_rpn(expr)
            print(f'Result: {result}\n')
        except Exception as e:
            print(f'Error: {e}\n')