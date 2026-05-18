class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)

        left = 0
        right = N - 1

        res = 0
        while left < right:
            curr_height = min(height[left], height[right])
            curr_width = right - left
            res = max(res, curr_height * curr_width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
