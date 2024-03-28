class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left < right:
            midpoint = left + (right - left) // 2
            if isBadVersion(midpoint):
                right = midpoint
            else:
                left = midpoint + 1
        return left
