"""
考点：数组的前缀和加速计算
"""

t = int(input())
for time in range(1, t+1):
    N,P = map(int, input().split())
    S = map(int, input().split()) #automaically recognize as an array?
    S = sorted(S, reverse=True) #sort in decreasing order

    # calculate prefix sum of an array
    psum = []
    psum.append(S[0])
    for i in range(1, len(S)):
        psum.append(psum[i-1]+S[i])
    #print(psum)

    min_time = float('inf')
    for i in range(N-P+1):
        total = P*S[i]
        """
        for j in range(i,i+P): #usual case, NOT USING PREFIX_SUM
            total -= S[j]
        """
        total -= (psum[i+P-1]-psum[i])
        total -= S[i]
        if total<min_time: min_time=total
    print("Case #{}: {}".format(time, min_time), flush = True)















"""
test:
3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7
"""