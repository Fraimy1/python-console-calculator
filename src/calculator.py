class Parser:
    def __init__(self, string=None):
        self.string = string
        self.data = self.parse_string(string) if string is not None else None
        
    def parse_string(self, string:str):
        if string is None:
            self.string = string

        data = [int(c) if c in '0123456789' else c for c in self.string.split()]
        
        return data

    def _add_to_stack(char, stack):
        pass
    
    def _get_precedence(char):
        match char:
            case '*':
                return 2
            case '/':
                return 2
            case '-':
                return 1
            case '+':
                return 1
            case '**':
                return 3
            case '(':
                return -1
            

    def infix_to_rpn(self, data):
        output = []
        stack = []
        # parentheses_indexes = []
        
        for c in data:
            if isinstance(c, int) or isinstance(c, float):
                output.append(c)
                continue
            
            if c == '(':
                stack.append(c)
                continue
            
            if c == ')':
                left_index = stack.index('(')
                output.extend(stack[left_index+1:])

            if not stack:
                stack.append(c)
                continue
            
            last_precedence = self._get_precedence(stack[-1])
            precedence = self._get_precedence(c)
            
            if  precedence == last_precedence:
                output.append(stack.pop())
                stack.append(c)
            elif None:
                pass
                # precedence based appending to output or stack 

            


if __name__ == '__main__':
    string = '3 + 4 * 2'
    parser = Parser(string)
    print(string)
    print(parser.parse_string(string))
