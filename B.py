t= int(input())
for cases in range(t):
  n= int(input())
  l= list(map(int,input().split()))
  '''since we need the maximum possible outcome therefore we will take the smaller numbers first.
  so that they have the least impact on the bigger numbers and we get maximum result'''
  
  #sorting the list in ascending order
  l.sort()
  
  #taking the smallest number i.e. the first number in the sorted list first
  #defining first or else when i am calling it it would give an error
  num = l[0]
  
  
  #slowly calculating the average in oncreasing order 
  #took // since we wanna get answer in float 
  for i in range(1, n):
    num = (num + l[i]) // 2 
    
  print(num)
  
  