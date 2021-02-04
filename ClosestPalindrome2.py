import time
start_time = time.time()

def Palindrome(Strnum):
    for i in range(len(Strnum) // 2):
        if Strnum[i] != Strnum[-1 - i]:
            return False
    return True
        
def convertNumIntoString(N):
	Strnum = str(N)
	return Strnum        

def ClosestPalindrome(N):
    change=-1
    #counter=0 (in case the original input is Palindrome and you need the next one)
    for i in range (N):        
        if Palindrome(convertNumIntoString(N)) == True:
            return N
            break
        else:
            #counter=1
            #print(N)
            N=N+change
            if change > 0:
                change+=1
                change=-change
            else:
                change-=1
                change=-change

#T=int(input("T: "))
T=1
for i in range(T):
    #N=int(input("N: "))
    N=1234567890123456
    print(ClosestPalindrome(N))
    print("--- %s seconds ---" % (time.time() - start_time))
