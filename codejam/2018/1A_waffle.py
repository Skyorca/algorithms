"""
first piece is to deal with smaller dataset with H=V=1
"""
import numpy as np

def count(grid):
    """
    grid is 2-d list
    """
    star='@'
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==star: c += 1
    return c

t = int(input())
for time in range(1, t+1):
    R,C,H,V = map(int, input().split())
    grid = list()
    for _ in range(R):
        r = input()
        r = [x for x in r]
        grid.append(r)
    grid = np.array(grid)
    #small dataset: H=V=1
    flag=0
    for i in range(R-1):  # if i=3, means cutting into (0,1,2,3)and(4,5,...)
        for j in range(C-1):
            p1 = grid[:i+1, :j+1] #top-left
            p2 = grid[:i+1, j+1:] #top-right
            p3 = grid[i+1:, :j+1] #bottom-left
            p4 = grid[i+1:, j+1:] #bottom-right
            c1 = count(p1)
            c2 = count(p2)
            c3 = count(p3)
            c4 = count(p4)
            #print(p1,p2,p3,p4)
            #print(c1,c2,c3,c4)
            if c1==c2==c3==c4: 
                flag=1
                break
    if flag==1: print("Case #{}: {}".format(time, 'POSSIBLE'), flush = True)
    else: print("Case #{}: {}".format(time, 'IMPOSSIBLE'), flush = True)














"""
test:
 	
6
3 6 1 1
.@@..@
.....@
@.@.@@
4 3 1 1
@@@
@.@
@.@
@@@
4 5 1 1
.....
.....
.....
.....
4 4 1 1
..@@
..@@
@@..
@@..
3 4 2 2
@.@@
@@.@
@.@@
3 4 1 2
.@.@
@.@.
.@.@

output:
Case #1: POSSIBLE
Case #2: IMPOSSIBLE
Case #3: POSSIBLE
Case #4: IMPOSSIBLE
Case #5: POSSIBLE
Case #6: IMPOSSIBLE


"""