t= int(input())
for cases in range(t):
  n = int(input())
  l= list(map(int,input().split()))
  flag=False  #for keeping track so that we can print the final outcome 
  for e in range(n-1):  
  #since we are comparing two consecutively positioned numbers 
  #therefore we are going from 0 to (n-1)th index 
  #otherwise it would try to compare the last number in the list to a number next to it which would cause an error
    if (l[e]%2==0) and (l[e+1]%2==0):
      flag=False 
      break
    elif (l[e]%2!=0) and (l[e+1]%2!=0):
      flag=False 
      break  
    else:
      flag=True 
      # break
    
  if flag:
    print("YES")
  else:
    print("NO")
  
'''logic here is that if at any position in the list , 
if we find that in the original list there are two adjacent even or odd numbers 
then in the sorted list a pair or consecutive evens or odds (alternative) will have different colours
which will defy the conditions provided'''
