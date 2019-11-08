"""
cut rop
using recursive: f(n)=max(f(i)f(n-i))
using dp
"""

def Recur2CutRope(length):
    """
    not work, anyway
    """
    if length == 1 or length==2 : return 1
    elif length == 3: return 2
    else:
        for i in range(1, length/2+1):
            return max(Recur2CutRope(i)*Recur2CutRope(length-i))

def Dp2CutRope(length):
    """
    """
    if length == 1 or length==2 : return 1
    elif length == 3: return 2
    dp = [0]*(length+1) #dp[i] stores the best solution at length i
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2 #当l>3时，2、3作为一个整体不切割，所以最优解是本身
    dp[3] = 3

    for i in range(4, length+1):
        max_v = 0
        for j in range(1, int(i/2)+1): #because of symmetry, i -> i/2
            l = dp[j]*dp[i-j]
            if l>max_v: max_v = l #find the maximum of dp[i]
        dp[i] = max_v # come to the conclusion of dp[i]
    print(dp)
    return dp[-1]

print(Dp2CutRope(8))