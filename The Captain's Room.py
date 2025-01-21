# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

# s = set(map(int, input().split()))

# l = list(s)

l = input().split()

# t = (len(l) - 1) / n
# print(s)
# print(l)
l.sort()
# print(l)
c = 1

s = set(l)
# print(s)

for i in range (len(l)-1):
    if l[i] == l[i+1] :
        c = c+1
        # print(c)
        
    elif l[i] != l[i+1] and c == n :
        # print(c)
        c = 1  
        s.remove(l[i])
        
        
    # else :
    #     print(l[i])
    
# print(s)

ans =  list(s)

print(ans[0])


#-------------above method got time exceeded error in some of the testcases

#--------------------correct method bellow


n = int(input())
d = dict()
l = list(map(int, input().split()))
for i in l:
    if i in d.keys():
        d[i] = d[i] + 1
    else :
        d[i] = 1
        
for x,y in d.items():
    if y == 1:
        print(x)
    
