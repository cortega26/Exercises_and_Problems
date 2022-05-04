#Replace all 0's with 5 for a given integer
#Practice problem for geeksforgeeks.org


def convert(n):
    new = []
    for i in str(n):
        if i == '0':
            new.append('5')
        else:
            new.append(i)
    #print(new)
    new = int(''.join(new))
    return new


if __name__=='__main__':
    n = int(input("What in the number? "))
    print(convert(n))
