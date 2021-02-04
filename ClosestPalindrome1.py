
def Palindrome(N):
    return int(str(N)[::-1])            

def ClosestPalindrome(N):
    change=-1
    for i in range (N+1):
        if int(Palindrome(N)) == N:
            return N
        else:
            N=N+change
            if change > 0:
                change+=1
                change=-change
            else:
                change-=1
                change=-change
               
import time
start_time = time.time()
#T=int(input())
T=1
for i in range(T):
    #N=int(input())
    N=1234567890123456
    print(ClosestPalindrome(N))
    print("--- %s seconds ---" % (time.time() - start_time))
