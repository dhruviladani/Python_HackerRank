def count_substring(string, sub_string):
    c = 0
    # a = 0
    # for i in range(0, len(string)):
    #     if string[i] == sub_string[0]:
            
    #         for j in range(0, len(sub_string)):
    #             i = i + 1
    #             a = a + 1
    #             string[i] == sub_string[j]
    #         c = c + 1
        
    #     i = i - a
    
    for i in range (0, len(string)):
        if string[i:i+len(sub_string)] == sub_string[0:] :
            c = c + 1
                
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
