import re
from src.errors import CalcError
from src.constants import pattern

TOKEN_RE2 = re.compile(pattern, re.VERBOSE)
Token = tuple[str, float | str]


class Parser:
    """Covnerts str RPN expression into tokens"""

    def parse(self, expr: str) -> list[tuple[str, float | str]]:
        """Parses str RPN expression into tokens using re pattern"""

        tokens = TOKEN_RE2.findall(expr)
        parsed: list[tuple[str, float | str]] = []
        for term in tokens:
            if term in {"+", "-", "*", "/", "**", "//", "%"}:
                parsed.append(("OP", term))
            elif term in "()":
                parsed.append(("PAR", term))
            else:
                try:
                    term = float(term)
                except ValueError:
                    raise CalcError(f"Couldn't convert {term} to float\n",
                                    f'Unsupported character "{term}"')
                parsed.append(("NUM", float(term)))

        return parsed
