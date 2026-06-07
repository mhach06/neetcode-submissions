class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        symbols = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            cur_el = tokens[i]

            if cur_el not in symbols:
                stack.append(int(cur_el))
            else:
                # Pop the second operand first (it was on top of the stack)
                num2 = stack.pop()
                # Pop the first operand second
                num1 = stack.pop()

                if cur_el == '+':
                    stack.append(num1 + num2)
                elif cur_el == '-':
                    stack.append(num1 - num2)
                elif cur_el == '*':
                    stack.append(num1 * num2)
                elif cur_el == '/':
                    # int() truncates toward zero in Python
                    stack.append(int(num1 / num2))
                
        return stack[0]
        