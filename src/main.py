from src.calculator import Calculator

user_welcome_message = """
=============================================
Welcome to the RPN calculator!

You can insert any RPN expression and the calculator will return the result.
e.g. "6 2 +" -> 8.0 or something crazy like "( 3 (4        (2)   -) ** )" -> 9.0
Calculator can (probably) handle it! 

Press Ctrl + C or type in "exit" to exit
=============================================
"""

user_goodbye_message = """
================

Goodbye!

================

"""

if __name__ == '__main__':
    calc = Calculator()
    print(user_welcome_message)
    while True:
        try: 
            expr = input("Insert your expression: ")
        except: 
            print('\n', user_goodbye_message)
            break
        if expr == "exit":
            print(user_goodbye_message)
            break

        try: 
            result = calc.calculate_rpn(expr)
            print(f'Result: {result}\n')
        except Exception as e:
            print(f'Error: {e}\n')