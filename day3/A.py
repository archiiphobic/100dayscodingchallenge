t= int(input())
for cases in range(t):
  n,s,x= map(int,input().split())
  l= list(map(int,input().split()))
  arr_sum = sum(l)
  if (arr_sum<= s) and ((arr_sum-s)%x==0):
    print("YES")
  else:
    print("NO")
    
'''logic: the array can only be appealing to DBMB if and only if :
1. the sum of the array is either less than or equal to the appealing sum 
(since we can only add something not substract)
2. the difference of the sum_array and the the appealing sum i.e. the amount to be increased 
is a multiple of the number we can increase i.e. x'''