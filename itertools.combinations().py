# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
a = list(input().split())
# print(a)
l = list(a[0])
l.sort()
l = ''.join(l)
# for i in l:
#     print(i)
for i in range(1,int(a[1])+1):
    
    ans = list(combinations(l,int(i)))
    for i in ans :
        print(''.join(i))


# print(ans)
