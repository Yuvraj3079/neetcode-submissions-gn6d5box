class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                print(f'While Stack: {stack}')
                index = stack.pop()
                result[index] = i - index
                print(f'result: {result}')

            stack.append(i)
            print(f'Ap Stack: {stack}')
        return result