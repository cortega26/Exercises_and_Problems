#Replace all 0's with 5 for a given integer
#Practice problem for geeksforgeeks.org


def convert(n):
    new = []
    for i in str(n):
        if i == '0':
            new.append('5')
        else:
            new.append(i)
    return int(''.join(new))


if __name__=='__main__':
    print("Do you want to include leading zeros (if exist)?")
    answer = input()
    if answer.upper() == "YES" or answer.upper() == "Y":
        n = str(input("What in the number? "))
        try:
            a = int(n)
            print(convert(n))
        except:
            print("Not a number. Program terminated.")
    elif answer.upper() == "NO" or answer.upper() == "N":
        try:
            n = int(input("What in the number? "))
            print(convert(n))
        except:
            print("Not a number. Program terminated.")
    else:
        print("Invalid answer. Program terminated.")
