t= int(input())
for cases in range(t):
  n,k= map(int,input().split())
  
  #if k=1 then we will have to substract it n times from the number n
  #since i raised to the power of any number equals 1 
  
  if k==1:
    print(n)
    
  else:
    #we are finding the largest power of k which is smaller than n
    #using while since we dont know how many iterations are there in this operation
    p = 1
    while p * k <= n:
        p *= k
    
    
    ans = 0    #this is to store the number of operations
    while p > 0:        
        ans += n // p  # counting the number of powers fitting in decreasing order
        n %= p         # sum left after removing the power from it
        p //= k        # reducing the power i.e. moving to the next smaller power than the largest
    print(ans)
    
  