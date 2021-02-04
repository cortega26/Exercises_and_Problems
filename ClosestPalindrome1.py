import time
start_time = time.time()

def Palindrome(N):
    N=int(str(N)[::-1])
    return N            

def ClosestPalindrome(N):
    change=-1
    for i in range (N+1):
        if int(Palindrome(N)) == N:
            return N
            break
        else:
            N=N+change
            if change > 0:
                change+=1
                change=-change
            else:
                change-=1
                change=-change

#T=int(input())
T=1
for i in range(T):
    #N=int(input())
    N=1234567890123456
    print(ClosestPalindrome(N))
    print("--- %s seconds ---" % (time.time() - start_time))
