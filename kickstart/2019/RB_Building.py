"""
考点： 字符串的前缀和计算字符频次
"""
from collections import defaultdict

t = int(input())
for time in range(1, t+1):
    N,Q = map(int, input().split())
    counter = 0
    string = input()
    alphabet = defaultdict(int)
    #do prefix efficient counting
    """
    say, s = "aabcbd"
    psum=[{a:1},{a:2},{a:2, b:1},{a:2,b:1,c:1},...]
    """
    psum = list()
    for c in string:
        alphabet[c] += 1
        psum.append(dict(alphabet)) #make sure to change defaultdict into dict 
    print(psum)
    for i in range(Q):
        l_idx, r_idx = map(int, input().split())
        odd_time = 0
        stop = 0
        for letter,freq in psum[r_idx-1].items():
            if letter not in psum[l_idx-2].keys():
                if freq%2==1:
                    if odd_time: 
                        stop += 1
                        break #odd>=2 false
                    else: odd_time += 1
            elif (freq-psum[l_idx-2][letter])%2==1:
                if odd_time: 
                    stop += 1
                    break #odd>=2 false
                else: odd_time += 1
        if not stop: counter += 1

    print("Case #{}: {}".format(time, counter), flush = True)

"""
test:
 
2
7 5
ABAACCA
3 6
4 4
2 5
6 7
3 7
3 5
XYZ
1 3
1 3
1 3
1 3
1 3
"""        
    