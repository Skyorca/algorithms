def isBeauty(x):
    """
    check whether all digits are even
    use recursive
    """
    if x<10: return not x%2==1
    else:
        return (isBeauty(x%10)) and (isBeauty(int(x/10)))


"""#N^2
N = int(input())
for n in range(1,N+1):
    num = int(input())
    for i in range(num+1): #upper bound is num and lower bound is 0
        if isBeauty(num+i) or isBeauty(num-i): 
            print("Case #{}: {}".format(n, i), flush = True)
            break
"""

#==================================Fast Version===============================================#
def detectFirstOdd(x):
    """
    given an int x, from the highest to lowest(left to right), find the first odd digit
    """
    s = str(x)
    for i in range(len(s)): # 0 to len(s)
        if int(s[i])%2==1: return i
    return -1 # no odd digit

N = int(input())
for n in range(1,N+1):
    num = int(input())
    min_v = num
    d = detectFirstOdd(num)
    if d==-1: 
        min_v=0 #no change happens
        print("Case #{}: {}".format(n, min_v), flush = True)
        continue
    else:
        s = str(num) #num->string
        s = [int(x) for x in s] #list of int, for concate, loop x through list and use str()+=x
        #deal with minus button
        s[d] -= 1
        for i in range(d+1,len(s)):
            s[i]=8
        new_num = str()
        for x in s:
            new_num += str(x)
        new_num = int(new_num)
        if num-new_num<min_v: min_v=num-new_num

        #deal with add button
        new_num = num
        while(not isBeauty(new_num)):
            d = detectFirstOdd(new_num)
            s = str(new_num) 
            s = [int(x) for x in s] 
            #case1: when d is 0 and s[d] is 9
            if d==0 and s[d]==9:
                s[d] = 0
                for i in range(d+1,len(s)):
                    s[i]=0
                new_num = str()
                for x in s:
                    new_num += str(x)
                new_num = '2'+new_num # 9... ->20...
                new_num = int(new_num)
                continue
            #case2: when d!=0 and s[d] is 9
            elif  d!=0 and s[d]==9: 
                s[d] = 0
                if s[d-1]!=8: s[d-1] += 2 #...69.. -> ...80...
                else: s[d-1] += 1 # ...89... -> ...90..., generate a new '9' and to be dealt with in the next loop
            
            #case3: usual cases
            else:
                s[d]+=1 #...6872345 ->...6880000

            for i in range(d+1,len(s)): #this piece is shared by csae 2&3
                s[i]=0
            new_num = str()
            for x in s:
                new_num += str(x)
            new_num = int(new_num)
    if min_v>new_num-num: min_v=new_num-num
    print("Case #{}: {}".format(n, min_v), flush = True)
    #print(new_num)
            





        





"""
test:
4
42
11
1
2018

4
4436271
6488962
88892
91112

"""


#print(isBeauty(26800864222680086122648))