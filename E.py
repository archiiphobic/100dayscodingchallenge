t= int(input())
for cases in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    for strings in range(m):
      s = input()
       # checking for first condition i.e. length should always match
      if len(s) != n:
        print("NO")
        continue
      #we will use two dictionaries to store the values
      num_to_char = {}
      char_to_num = {}
      possible = True      #flag
            
      for i in range(n):
          val = a[i]
          char = s[i]
                
          # Checking if this number has been assigned to a different character before
          if val in num_to_char:
              if num_to_char[val] != char:
                  possible = False
                  break
          else:
              num_to_char[val] = char
                    
          # Checking if this character has been assigned to a different number before
          if char in char_to_num:
              if char_to_num[char] != val:
                  possible = False
                  break
          else:
              char_to_num[char] = val
            
      if possible:
          print("YES")
      else:
          print("NO")
