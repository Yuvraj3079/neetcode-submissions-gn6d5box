import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv}
        for s in tokens:
            #print(s)
            if s in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                res = operators[s](b, a)
                stack.append(res)
                #print(f'a; {a}, b: {b}, res: {res}')
            else:
                stack.append(s)

        return int (stack[-1])
