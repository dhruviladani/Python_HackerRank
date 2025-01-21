# n = int(input())
# s = set(map(int, input().split()))

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

s = set(map(int, input().split()))

m = int(input())

for i in range(m):
    c = input().split()
    
    if c[0] == 'remove' :
        s.remove(int(c[1]))
        
    elif c[0] == 'discard' :
        s.discard(int(c[1]))
        
    else :
        s.pop()
        
ans = list(s)
sum = 0
for i in range(len(s)):
    sum = sum + ans[i]
    
print(sum)
    
    
