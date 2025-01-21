# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()

set1 = set(map(int, input().split()))

m = input()

set2 = set(map(int, input().split()))

ans = set1.union(set2)
# print(ans)
print(len(ans))
