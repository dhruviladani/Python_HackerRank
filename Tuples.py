if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # l = []

    # for i in range(n):
        
    #     l.append(i)
        
    # t = tuple(l)
    # print(hash(t))
    
    t = tuple(integer_list)
    print(hash(t))
    
