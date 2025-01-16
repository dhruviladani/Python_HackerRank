

def split_and_join(line):
    s = line.replace(" ","-")
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
