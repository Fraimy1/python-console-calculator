class Parser:
    def __init__(self, string=None):
        self.string = string
        self.data = self.parse_string(string) if string is not None else None
        
    def parse_string(self, string:str):
        if string is None:
            self.string = string
        self.string = self.string.replace('(', ' ( ').replace(')', ' ) ')
        data = [int(c) if c in '0123456789' else c for c in self.string.split()]
        data = [el for el in data if el != ' ']
        
        return data

    def _add_to_stack(char, stack):
        pass
    
    def _get_precedence(self, char):
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
            

    def infix_to_rpn(self, data = None):
        output = []
        stack = []
        # parentheses_indexes = []
        
        if data is not None:
            self.data = data

        for c in self.data:
            if isinstance(c, int) or isinstance(c, float):
                output.append(c)
                print(f'char: {c} | stack: {stack} | output: {output}')
                continue
            
            if c == '(':
                stack.append(c)
                print(f'char: {c} | stack: {stack} | output: {output}')
                continue
            
            if c == ')':
                left_index = stack.index('(')
                output.extend(stack[left_index+1:])
                del stack[left_index+1:]
                stack.pop(left_index)
                continue

            if not stack:
                stack.append(c)
                print(f'char: {c} | stack: {stack} | output: {output}')
                continue
            
            last_precedence = self._get_precedence(stack[-1])
            precedence = self._get_precedence(c)

            print(stack[-1], last_precedence if last_precedence is not None else '')
            print(c, precedence if precedence is not None else '')
            
            if  precedence == last_precedence:
                output.append(stack.pop())
                stack.append(c)
            elif last_precedence>precedence:
                output.append(stack.pop())
                stack.append(c)
            else:
                stack.append(c)
                # precedence based appending to output or stack 

            print(f'char: {c} | stack: {stack} | output: {output}')
        
        while stack:
            output.append(stack.pop())

        print(f'stack: {stack} | output: {output}')
        return output

            


if __name__ == '__main__':
    tests = [
        '3 + 2',
        '3 + 4 * 2'
        '(3 + 4) * 2'
    ]

    for test in tests:
        parser = Parser(test)
        print(test, 'eval result =', eval(test))
        print(parser.parse_string(test))
        print(parser.infix_to_rpn(test))
