t= int(input())
for cases in range(t):
  country = input().split()
  new_name=""
  for word in country:
    new_name+=(word[0])
  print(new_name)