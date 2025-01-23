# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a = list(input().split())
# print(a)
l = list(a[0])
l.sort()
# print(l)
l = ''.join(l)
ans = list(permutations(l,int(a[1])))

for i in ans :
    print(''.join(i))

# print(ans)
