import re
from errors import CalcError

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
Token = tuple[str, float | None]

class Parser:
    """Covnerts str RPN expression into tokens"""
    def __init__(self):
        self.smth = None

    def parse(self, expr: str):
        """Parses str RPN expression into tokens using re pattern"""
        
        if not expr or not expr.strip():
            raise CalcError("Empty expression")
        
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