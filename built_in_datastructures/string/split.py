def split_and_join(line):
    # write your code here
    a = line.split(' ')
    l = "-".join(a)
    return l


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
