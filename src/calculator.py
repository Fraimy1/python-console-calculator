from parser import Parser
from errors import CalcError

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
                    raise CalcError("Not enough operands")
                b = st.pop()      
                a = st.pop()       
                if value == "+": st.append(a + b)
                elif value == "-": st.append(a - b)
                elif value == "*": st.append(a * b)
                elif value == "%": st.append(a % b)
                elif value == "**": st.append(a**b)
                elif value == "//":
                    if b == 0:
                        raise CalcError("Division by zero")
                    st.append(a // b)
                elif value == "/":
                    if b == 0:
                        raise CalcError("Division by zero")
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
            elif tok_type == 'NUM':
                try:
                    st.append(float(value))
                except ValueError:
                    raise CalcError(f"Not a number or operator: {value}")
            
        if len(st) != 1:
            raise CalcError("Excess data in expression")
    
        if paren_marks:
            raise CalcError(f"Mismatched parentheses: {len(paren_marks)} '(' were never closed")

        result = st[0]        
        
        if isinstance(result, complex):
            raise CalcError('No solution in real numbers')
        
        return result