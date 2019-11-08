import numpy as np
from collections import deque
input = [1,3,2,3,1,4]

def DpOfLIS(nums):
        if len(nums)==0: return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i+1):
                if nums[i]>nums[j]: 
                    if dp[i]<dp[j]+1: dp[i]=dp[j]+1
        return max(dp)

def StackofLIS(nums):
    """
    use a stack to store longest increasing subarray
    """
    s = deque([nums[0]])
    for i in range(1, len(nums)):
        if nums[i]>s[-1]: #nums[i]>栈顶元素，则入栈
            s.append(nums[i])
        else: #else, use smaller nums[i] to replace elements in stack to make sure the length go furthur
            for j in range(len(s)):
                if s[j]>= nums[i]: #must be larger or equal to 
                    s[j] = nums[i]
                    break
        print(s)
    return len(s)

print(StackofLIS([1,3,2,3,1,4]))

