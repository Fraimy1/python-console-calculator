from src.parser import Parser
from src.errors import CalcError

class Calculator:
    """Calculates RPN expressions using expression parsed by Parser.parse()"""
    def __init__(self) -> None:
        self.parser = Parser()

    def calculate_rpn(self, expr: str) -> float:
        """Calculates RPN and returns result"""
                
        expr = self.parser.parse(expr)

        stack: list[float] = []
        
        paren_marks = [] # marks the point where parentheses open

        for tok_type, value in expr:
            if tok_type == 'OP':
                if len(stack) < 2:
                    raise CalcError("Not enough operands")
                b = stack.pop()      
                a = stack.pop()       
                if value == "+": stack.append(a + b)
                elif value == "-": stack.append(a - b)
                elif value == "*": stack.append(a * b)
                elif value == "%": 
                    if b == 0:
                        raise CalcError("Division by zero")
                    stack.append(a % b)
                elif value == "**": 
                    power_res = a**b
                    if isinstance(power_res, complex):
                        raise CalcError(f'No solution in real numbers for {a} ** {b}')
                    stack.append(power_res)
                elif value == "//":
                    if b == 0:
                        raise CalcError("Division by zero")
                    stack.append(a // b)
                elif value == "/":
                    if b == 0:
                        raise CalcError("Division by zero")
                    stack.append(a / b)
            elif tok_type == 'PAR':
                if value == '(':
                    paren_marks.append(len(stack))
                else:
                    if not paren_marks:
                        raise CalcError('The parentheses were never opened')
                    paren_size = len(stack) - paren_marks.pop()
                    if paren_size != 1:
                        raise CalcError(f'Incorrect parentheses expression. Expected format is (2) or (2 1 +)')
            elif tok_type == 'NUM':
                try:
                    stack.append(float(value))
                except ValueError:
                    raise CalcError(f"Not a number or operator: {value}")
            
        if len(stack) != 1:
            raise CalcError("Excess data in expression")
    
        if paren_marks:
            raise CalcError(f"Mismatched parentheses: {len(paren_marks)} '(' were never closed")    
        
        return stack[0] 