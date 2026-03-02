t = int(input())
for cases in range(t):
    n, r = map(int,input().split())
    a = list(map(int,input().split()))
    
    #counting the total number of people in all families
    total_people = sum(a)
    
    #counting the number of pairs. since these people will always be happy
    total_pairs=0
    for people in a:
      total_pairs+= people //2
    
    #counting the number of people who are left single in a family
    #these people are happy only if number of rows remaining after assigning 
    #them to the pairs is greater than the number of single people. 
    #if no empty row is left then they will have to share seats which will make them unhappy
    single_people=0
    for people in a:
      single_people += people%2 

    #counting the number of rows available after all pairs are seated
    remaining_rows = r - total_pairs
    
    # If single people fit in the remaining rows (one person per row),
    # all single people are happy. 
    #and if they dont fit then each remaining person is ruining the happiness of someone else as well :)
    if single_people <= remaining_rows:
        print(total_people)
    else:
        #these people will have to sit with strangers i.e. be unhappy
        unhappy = single_people - remaining_rows
        print(total_people - 2 * unhappy)