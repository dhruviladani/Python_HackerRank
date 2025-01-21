# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())

a = set(map(int, input().split()))

n = int(input())

b = set(map(int, input().split()))

ans = b ^ a

final = list(ans)
final.sort()
for i in range(len(final)):
    print(final[i])
