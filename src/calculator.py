import re
import operator

NUM = r"\d+(?:\.\d+)?"

pattern = rf"""
    \s*
    (
        \*\*            |   # двойная *
        //              |   # двойной /
        \*(?!\*)        |   # одиночная *
        /(?!/)          |   # одиночный /
        [+\-()%]        |   # одиночные токены: + - ( ) %
        {NUM}               # число
    )
"""

TOKEN_RE2 = re.compile(pattern, re.VERBOSE)

class Parser:
    def __init__(self, string=None):
        self.string = string
        self.data = self.parse_string(string) if string is not None else None
        
    def parse(self, expr: str) -> list[str] | None:
        expr = TOKEN_RE2.findall(expr)
        parsed = []
        print('parsed expression:', expr)

        for term in expr:
            if term.isnumeric():
                parsed.append(("NUM", float(term)))
            elif term in {"+", "-", "*", "/", "**", "//"}:
                parsed.append(("OP", term))
            elif term in "()":
                parsed.append(("PAR", term))
            else:  
                return None
        return parsed

Token = tuple[str, float | None]

class CalcError():
    pass

class Calculator:
    def __init__(self):
        self.parser = Parser()

    OPS = {"+", "-", "*", "/"}

    def calculate_rpn(self, expr: str) -> float:
        if not expr or not expr.strip():
            raise CalcError("Пустой ввод")
        
        expr = self.parser.parse(expr)

        st: list[float] = []
        
        print(expr)

        for tok_type, value in expr:
            if tok_type == 'OP':
                if len(st) < 2:
                    raise CalcError("Недостаточно операндов")
                b = st.pop()       # второе число
                a = st.pop()       # первое число
                if value == "+": st.append(a + b)
                elif value == "-": st.append(a - b)
                elif value == "*": st.append(a * b)
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
                ...
            elif tok_type == 'NUM':
                try:
                    st.append(float(value))
                except ValueError:
                    raise CalcError(f"Not число и не оператор: {value}")

        if len(st) != 1:
            raise CalcError("Лишние данные в выражении")
        return st[0]

if __name__ == '__main__':
    calc = Calculator()
    tests = [
        '3 2 4 ** +',          # 3 + (2 ** 4) = 19
        '5 1 2 + 4 ** + 3 -',  # 5 + (1 + 2) ** 4 - 3 = 83
        '10 3 // 2 *',         # (10 // 3) * 2 = 6
        '20 3 % 2 +',          # (20 % 3) + 2 = 4
        '2 3 + 4 *',           # (2 + 3) * 4 = 20
        '2 3 4 * +',           # 2 + (3 * 4) = 14
        # parentheses / sign tests
        # '+2' should parse as positive 2
        '2 +2 +',              # 2 + (+2) = 4
        # '-78' should parse as negative 78
        '5 -78 +',             # 5 + (-78) = -73
        # with parentheses equivalent
        '3 ( 2 1 + ) *',       # 3 * (2 + 1) = 9
        '6 ( 2 3 ** ) /'       # 6 / (2 ** 3) = 0.75
    ]
    for test in tests:
        print(calc.calculate_rpn(test))