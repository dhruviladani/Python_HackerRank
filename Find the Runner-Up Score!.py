if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = -101
    
    for i in range(n):
        
        if m < arr[i] :
            m = arr[i]
    
    arr.sort()
    ans = 0
    for i in range(n):
        if arr[i] < m:
            ans = arr[i]
        else :
            break
            
    print(ans)
