t= int(input())
for cases in range(t):
  #its all about whether the sections overlap or not 
  l,r= map(int,input().split())
  L,R= map(int,input().split())
  left_overlap = max(l, L)
  right_overlap = min(r, R)
  #case1: no overlap , when right of one is less than left of another
  if left_overlap > right_overlap:
    print(1)
  else:
  #case2: there is an overlap
    ans= right_overlap-left_overlap
    #if the lefmost room is in left of the overlap 
    #then we need to close one more door to the left
    if min(l, L) < left_overlap:
        ans += 1
        
    #if the rightmost room is in the right of the overlap
    #we need to close one more door to the right
    if max(r, R) > right_overlap:
        ans += 1
    print(ans)
  
  