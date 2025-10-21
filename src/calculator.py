from src.parser import Parser
from src.errors import CalcError
from src.validator import Validator

class Calculator:
    """Calculates RPN expressions using expression parsed by Parser.parse()"""

    def __init__(self, parser = Parser(), validator = Validator()) -> None:
        self.parser = parser
        self.validator = validator

    def calculate_rpn(self, expr: str) -> float:
        """Calculates RPN and returns result"""

        tokens: list[tuple[str, float | str]] = self.parser.parse(expr)
        self.validator.check_tokens(tokens)
        stack: list[float] = []

        for tok_type, value in tokens:
            if tok_type == "OP":
                b = stack.pop()
                a = stack.pop()
                if value == "+":
                    stack.append(a + b)
                elif value == "-":
                    stack.append(a - b)
                elif value == "*":
                    stack.append(a * b)
                elif value == "%":
                    if b == 0:
                        raise CalcError("Division by zero")
                    stack.append(a % b)
                elif value == "**":
                    power_res = a**b
                    if isinstance(power_res, complex):
                        raise CalcError(f"No solution in real numbers for {a} ** {b}")
                    stack.append(power_res)
                elif value == "//":
                    if b == 0:
                        raise CalcError("Division by zero")
                    stack.append(a // b)
                elif value == "/":
                    if b == 0:
                        raise CalcError("Division by zero")
                    stack.append(a / b)
            elif tok_type == "NUM":
                stack.append(float(value))

        return stack[0]
