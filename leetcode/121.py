"""
把数组两点求差问题转化成最大子序列和，借助牛顿莱布尼兹公式。
数组求导就是前减去后。
"""


def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1 or len(prices)==0: return 0
        diff = list()
        for i in range(1, len(prices)):
            diff.append(prices[i]-prices[i-1])
        
        dp = [0]*len(prices)
        dp[0]=max(0,diff[0])
        for i in range(1,len(diff)):
            dp[i]=max(0, dp[i-1]+diff[i])
        return max(dp)