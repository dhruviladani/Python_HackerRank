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
    if i[0] in count.keys() and count[i[0]] > 0 :
        count[i[0]] -= 1
        # print(count[x])
        ans = ans + i[1]
        # print(ans)
    
print(ans)

