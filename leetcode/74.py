"""
求不含重复元素的子集（不能重复）
位运算：虽然是O(2^N*N)不过因为是位运算所以很快？
回溯
"""

def Bit2subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        result = []
        n = 1<<size #n=2^size
        for i in range(n): 
            tmp = []
            for j in range(size):
                if (i>>j)&1:tmp.append(nums[j])
            result.append(tmp)
        return result
"""
其实就是穷举任意一位是0/1。关键是怎么把一个01状态如【A B C】时的状态【1 0 1】和[A C]对应起来
这里可以将状态01串依次向右移位后与1做与运算。右移i次后与1做与运算结果是1说明原串的n-i-1位在里面。
"""
