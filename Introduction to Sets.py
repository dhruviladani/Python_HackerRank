def average(array):
    add = 0
    array.sort()
    c = 1
    for i in range(0,len(array)-1):
        if i == len(array)-1 or array[i] != array[i+1]:
            
            add += array[i]
            c += 1
        
    add += array[-1]
    avg = add / c
    
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
