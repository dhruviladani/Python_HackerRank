# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())

l = list(map(int, input().split()))

m = int(input())

count = Counter(l)

# print(count)

l2 = list()
for i in range(m):
    l2.append(list(map(int,(input().split()))))
   
# print(l2)
ans = 0
for i in l2:
    for x,y in count.items():
        
        if int(y) > 0 and i[0] == x :
            count[x] -= 1
            # print(count[x])
            ans = ans + i[1]
            # print(ans)
    
print(ans)

