# https://practice.geeksforgeeks.org/problems/replace-all-0-with-5-in-an-input-integer/1/


def convert(n):
    """
    Given a number n, this script will replace all 0's with 5's
    """
    
    new = ""
    for i in str(n):
        if i == '0': new += '5'
        else: new += i
    return int(new)


if __name__=='__main__':
    convert(34892034890)
