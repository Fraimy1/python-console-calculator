import re
import operator

NUM = r"[+-]?[\d_]+(?:\.[\d_]+)?"

pattern = rf"""
    \s*
    (
        \*\*            |   # двойная *
        //              |   # двойной /
        %               |   # одиночный %
        \*(?!\*)        |   # одиночная *
        /(?!/)          |   # одиночный /
        {NUM}            |   # число с возможным знаком
        [*/()%]          |   # одиночные токены кроме + -
        [+\-]                # + или - как отдельный оператор
    )
"""

TOKEN_RE2 = re.compile(pattern, re.VERBOSE)

class Parser:
    def __init__(self):
        self.smth = None

    def parse(self, expr: str):
        expr = TOKEN_RE2.findall(expr)
        print('parsed expression:', expr)

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
    def __init__(self):
        self.parser = Parser()

    def calculate_rpn(self, expr: str) -> float:
        if not expr or not expr.strip():
            raise CalcError("Пустой ввод")
        
        expr = self.parser.parse(expr)

        print(f'{expr=}')
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
    print(calc.calculate_rpn('1_000_000.132_123 2 +'), 2**(2**3), (2**2)**3)
    # print(1.2_2_3)