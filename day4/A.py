t= int(input())                   #taking in number of test cases
for cases in range(t):
  s = input()                #our input string - can either be formatted as "RxCy" or "RRCC"      
  flag = False                #this flag will only be true when the input string is in "RxCy" format
  if ((s[0] == 'R') and ('0' <= s[1] <= '9')):                 #checking if the first character is R and the next character is a number
    #we are checking if our input string has a C in it, which would confirm that the string is in "RxCy" format
    for i in range(2, len(s)):                                 
      if s[i] == 'C':
        flag = True

    #case 1: RxCy --> RRCC
  if flag:
    col = s.find('C')      #finding the index of C in the string
    row = s[1:col]         #the row number is the substring between R and C
    column = int(s[col+1:])        #the column number is the substring after C, which we convert to an integer
 

   #logic: every 26 letter represents a new "digit" in the column number, so we can repeatedly divide the column number by 26 to find the corresponding letters
   #for example, if the column number is 27, we would have 1 "digit" of A and 1 "digit" of A, which would give us the column string "AA"
   #thus the remainder when dividing by 26 gives us the letter for that "digit", and we can continue dividing until we have processed all "digits" in the column number

    col_str = ""
    while column > 0:
      column -= 1   #substracting 1 from column to make it 0-indexed , since if get 1 as the column number, we want to get A, which is the 0th letter in the alphabet
      col_str = chr(ord('A') + (column % 26)) + col_str
      column //= 26     #dividing column by 26 to move on to the next "digit"
        
    print(col_str + row)
        
    #case 2: RRCC --> RxCy 
  else:
    letters = ""
    digits = ""
    for char in s:
      if ('A' <= char <= 'Z'):
        letters += char
      else:
        digits += char

    #logic: we multiply the column number by 26 for each letter in the column string, and add the value of the letter (where A=1, B=2, ..., Z=26) to get the total column number
    column = 0
    for char in letters:
      column = column * 26 + (ord(char) - ord('A') + 1)
            
    print("R" + digits + "C" + str(column))