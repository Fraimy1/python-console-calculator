import re

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

TOKEN_RE2 = re.compile(pattern, re.VERBOSE)

class Parser:
    """Covnerts str RPN expression into tokens"""
    def __init__(self):
        self.smth = None

    def parse(self, expr: str):
        """Parses str RPN expression into tokens using re pattern"""

        expr = TOKEN_RE2.findall(expr)

        parsed = []
        for term in expr:
            if re.fullmatch(NUM, term):
                parsed.append(("NUM", float(term)))
            elif term in {"+", "-", "*", "/", "**", "//", "%"}:
                parsed.append(("OP", term))
            elif term in "()":
                parsed.append(("PAR", term))
            else:
                raise CalcError(f'Unsupported character "{term}"')
        return parsed

Token = tuple[str, float | None]

class CalcError(Exception):
    pass

class Calculator:
    """Calculates RPN expressions using expression parsed by Parser.parse()"""
    def __init__(self) -> None:
        self.parser = Parser()

    def calculate_rpn(self, expr: str) -> float:
        """Calculates RPN and returns result"""
        
        if not expr or not expr.strip():
            raise CalcError("Пустой ввод")
        
        expr = self.parser.parse(expr)

        st: list[float] = []
        
        paren_marks = [] # marks the point where parentheses open

        for tok_type, value in expr:
            if tok_type == 'OP':
                if len(st) < 2:
                    raise CalcError("Недостаточно операндов")
                b = st.pop()      
                a = st.pop()       
                if value == "+": st.append(a + b)
                elif value == "-": st.append(a - b)
                elif value == "*": st.append(a * b)
                elif value == "%": st.append(a % b)
                elif value == "**": st.append(a**b)
                elif value == "//":
                    if b == 0:
                        raise CalcError("Деление на ноль")
                    st.append(a // b)
                elif value == "/":
                    if b == 0:
                        raise CalcError("Деление на ноль")
                    st.append(a / b)
            elif tok_type == 'PAR':
                if value == '(':
                    paren_marks.append(len(st))
                else:
                    if not paren_marks:
                        raise CalcError('The parentheses were never opened')
                    paren_size = len(st) - paren_marks.pop()
                    if paren_size != 1:
                        raise CalcError(f'Incorrect parentheses expression. Expected format is (2) or (2 1 +)')
                    # opened_par_count -= 1
            elif tok_type == 'NUM':
                try:
                    st.append(float(value))
                except ValueError:
                    raise CalcError(f"Not a number or operator: {value}")
            
        if len(st) != 1:
            raise CalcError("Лишние данные в выражении")
        
        if paren_marks:
            raise CalcError(f"Mismatched parentheses: {len(paren_marks)} '(' were never closed")

        return st[0]

if __name__ == '__main__':
    calc = Calculator()
    parser = Parser()
    tests = [
    ('3 2 4 ** +', 19),
    ('5 1 2 + 4 ** + 3 -', 83),
    ('10 3 // 2 *', 6),
    ('20 3 % 2 +', 4),
    ('2 3 + 4 *', 20),
    ('2 3 4 * +', 14),
    ('2 +2 +', 4),
    ('5 -78 +', -73),
    ('3 2 1 + *', 9),
    ('6 2 3 ** /', 0.75),
]
    print(calc.calculate_rpn('(3 (1_000_000.132_123 2 +) *)'))