if __name__ == '__main__':
    s = input()
    isalnum = False
    for i in s :
        if i.isalnum():
            isalnum = True
    print(isalnum)
    
    isalpha = False
    for i in s :
        if i.isalpha():
            isalpha = True
    print(isalpha)
    
    isdigit = False
    for i in s :
        if i.isdigit():
            isdigit = True
    print(isdigit)
    
    islower = False
    for i in s :
        if i.islower():
            islower = True
    print(islower)
    
    isupper = False
    for i in s :
        if i.isupper():
            isupper = True
    print(isupper)
        
    
    
    # print(s.isalnum())
    # print(s.isalpha())
    # print(s.isdigit())
    # print(s.islower())
    # print(s.isupper())
