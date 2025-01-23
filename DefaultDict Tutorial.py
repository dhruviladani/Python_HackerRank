# Enter your code here. Read input from STDIN. Print output to STDOUT

n = list(input().split())
# print(n)

a = []
for i in range(int(n[0])):
    # a.append(input().split())
    a = a + input().split()
    
# print(a)

b = list()
for i in range(int(n[1])):
    # b.append(input().split())
    b = b + input().split()
# print(b)

for i in range (int(n[1])) :
    if b[i] not in a :
        print(-1,end=' ')
        print()
        
    else:
        for j in range(int(n[0])) :
        
            if str(b[i]) == str(a[j]) :
                print(j+1,end=' ')
        print()
    
    
