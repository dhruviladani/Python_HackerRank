
n = input()

set1 = set(map(int, input().split()))

m = input()

set2 = set(map(int, input().split()))

ans = set1 - set2
# ans = set1.difference(set2)

# print(ans)
print(len(ans))
