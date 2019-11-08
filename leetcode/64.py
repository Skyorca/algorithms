from collections import deque

def BFS2minPathSum(grid):
    """
    grid: list[list[int]], m*n
    BFS will exhaust time for big arrays but ran ok
    """
    path = deque([(0,0)]) #store the coordinate of points
    length = deque([grid[0][0]])

    def __same(q,dst):
        if len(set(list(q)))==1 and set(list(q)).pop() == dst: return 1
        else: return 0

    end = 0
    dst = (len(grid)-1, len(grid[-1])-1)
    if len(path)==0: return length.pop() #[[0]]这种
    while(not end):
        e = path.pop()
        x,y = e[0],e[1]
        if x+1<len(grid): 
            path.appendleft((x+1, y)) #go down
            pre_len = length[-1]
            length.appendleft(pre_len+grid[x+1][y])
        if y+1<len(grid[x]): 
            path.appendleft((x,y+1)) #go right
            pre_len = length[-1]
            length.appendleft(pre_len+grid[x][y+1])
        
        length.pop()
        print(path, length)
        end = __same(path, dst)
    print(length)
    return min(list(length))

def Dp2minPathSum(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue # start point
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j] #first row
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j] #first column
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j] #inner parts
        return grid[-1][-1]

    

input1 = [[1,3,1],[1,5,1],[4,2,1]]
input2 = [[1,2,5],[3,2,1]]
input3 = [[6,2,4,4,6,2,2,9],[6,4,5,1,0,8,3,5],[9,3,0,5,9,8,1,7],[7,9,9,3,1,9,1,9],[3,7,5,0,0,8,9,8],[4,6,9,4,4,3,0,4],[6,2,9,7,2,3,5,9],[2,4,3,5,5,6,5,9],[3,0,1,5,0,0,4,5],[9,3,9,3,8,1,7,6]]
print(Dp2minPathSum(input3))