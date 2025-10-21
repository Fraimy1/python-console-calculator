from src.errors import CalcError

class Validator:

    @staticmethod
    def check_tokens(tokens:list[tuple[str, float | str]]):
        stack_size = 0 # current size of stack
        paren_open_count = 0
        paren_marks:list[int] = [] # check how many operands are inside parentheses

        if not tokens:
            raise CalcError("Empty expression")

        for tok_type, value in tokens:
            if tok_type == "NUM":
                stack_size += 1
            elif tok_type == "OP":
                if stack_size < 2:
                    raise CalcError(f"Not enough values before operator: {stack_size} (Requires 2)")
                stack_size -= 1
            elif tok_type == "PAR":
                if value == ')':
                    if paren_open_count < 1:
                        raise CalcError("Parentheses were never opened")

                    # Expression inside parentheses should give one number as a result
                    last_stack_size = paren_marks.pop()
                    paren_result_len = stack_size - last_stack_size

                    if paren_result_len != 1:
                        raise CalcError("Invalid expression inside parentheses\n"
                                        f"Extra characters in parentheses: {paren_result_len-1}\n"
                                        "Expected format is (2) or (2 1 +)")
                    paren_open_count -=1

                if value == "(":
                    paren_marks.append(stack_size)
                    paren_open_count += 1

        if paren_open_count != 0:
            raise CalcError(f"Mismatched parentheses: Unclosed parentheses count = {paren_open_count}")

        if stack_size != 1:
            raise CalcError("Expression doesn't reduce to one value (is unsolveable).\n"
                            f"Number of extra tokens = {stack_size-1}")

        return True
