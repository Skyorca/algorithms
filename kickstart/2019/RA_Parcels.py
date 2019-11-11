"""
only deals with small dataset
"""
import copy

t = int(input())

for time in range(1, t+1):
    R, C = map(int, input().split())
    grid = list()
    for _ in range(R):
        r = str(input())
        r = [int(x) for x in r]
        grid.append(r)
    #step1: loop through all grid and calculate the min dist
   # mindist = [[0]*C]*R #这个写法极其害人，会保留复制的索引，动一个被复制到其他位置的也会变
    mindist_old = list()
    for _ in range(R):
        mindist_old.append([0]*C)
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1: continue
            else: 
                min_v = float('inf')
                for p in range(R):
                    for q in range(C):
                        if grid[p][q]==1: 
                            if abs(p-i)+abs(q-j)<min_v: min_v=abs(p-i)+abs(q-j)
                mindist_old[i][j]=min_v
    #stage2: add one new delivery each time
    res = float('inf')
    is_office = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j]==1: is_office=1
            mindist_new = copy.deepcopy(mindist_old)
            grid[i][j]=1 #set a delivery here
            for p in range(R):
                for q in range(C):
                    mindist_new[p][q] = min(mindist_new[p][q], abs(p-i)+abs(q-j)) #could a delivery time decrease due to new office in (i,j)
            min_tmp = max([max(x) for x in mindist_new]) #new overall delivery time
            if not is_office:grid[i][j]=0 #clear
            if min_tmp<res: res=min_tmp
            is_office=0 #clear
                
    print("Case #{}: {}".format(time, res), flush = True)
                



"""
test:

3
3 3
101
000
101
1 2
11
5 5
10001
00000
00000
00000
10001

out:
1
0
2
"""