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



# 2nd method -----------------


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    arr1 = sorted(arr,reverse=True)
    
    for i in range (0, len(arr)) :
        if (arr1[i] == arr1[i+1]):
            continue
        else:
            print(arr1[i+1])
            break
        
