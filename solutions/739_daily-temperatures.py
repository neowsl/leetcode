class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)

        answer = [0] * N
        # monotonic stack of tuple (index, temperature)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_index = stack.pop()[0]
                answer[prev_index] = i - prev_index

            stack.append((i, temp))

        return answer
