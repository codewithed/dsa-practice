class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, soln = [],[]

        def backtrack(i):
            if i == n:
                res.append(soln[:])
                return
            backtrack(i+1)
            soln.append(nums[i])
            backtrack(i+1)
            soln.pop()
            

        backtrack(0)
        return res  
