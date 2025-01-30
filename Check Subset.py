# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for i in range(n):

    a = int(input())
    s1 = set(map(int, input().split()))
    b = int(input())
    s2 = set(map(int, input().split()))
    
    print(s1.issubset(s2))
