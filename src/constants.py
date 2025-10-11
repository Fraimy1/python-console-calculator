NUM = r"[+-]?[\d_]+(?:\.[\d_]+)?"

pattern = rf"""
    \s*
    (
        \*\*            |   # Double *
        //              |   # Double /
        %               |   # solo %
        \*(?!\*)        |   # solo *
        /(?!/)          |   # solo /
        {NUM}           |   # Number
        [*/()%]         |   # tokens except + -
        [+\-]               # + or - as separate operators
    )
"""

USER_WELCOME_MESSAGE = """
=============================================
Welcome to the RPN calculator!

You can insert any RPN expression and the calculator will return the result.
e.g. "6 2 +" -> 8.0 or something crazy like "( 3 (4        (2)   -) ** )" -> 9.0
Calculator can (probably) handle it!

Press Ctrl + C or type in "exit" to exit
=============================================
"""

USER_GOODBYE_MESSAGE = """
================

Goodbye!

================

"""
