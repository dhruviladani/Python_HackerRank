# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set(map(int, input().split()))
# print(s)
m = int(input())
for i in range(m):
    a = input().split()
    b = set(map(int, input().split()))
    
    if (a[0] == 'update'):
        s.update(b)
        # print(s)
        
    elif(a[0] == 'intersection_update'):
        s.intersection_update(b)
        # print(s)

        
    elif (a[0] == 'difference_update'):
        s.difference_update(b)
        # print(s)
        
        
    else:
        s.symmetric_difference_update(b)
        # print(s)
        
ans = sum(s) 
print(ans)
        
