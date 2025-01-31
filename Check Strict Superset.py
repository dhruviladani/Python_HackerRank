# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int, input().split()))
n = int(input())

flag = False
for i in range(n):
    x = set(map(int, input().split()))
    
    flag = x.issubset(a)
    if (flag == False):
        break
    
print(flag)
