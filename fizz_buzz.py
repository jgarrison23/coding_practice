#fizzbuzz hw


#set initial count to 0
count = 0

for count in range (1,101):
    #check if count is a multiple of 3 and 5. If so, print fizzbuzz
    if count % 3 == 0 and count % 5 == 0:
        print ("fizzbuzz")

    #check if count is multipe of 3. If so, print fizz
    elif count % 3 == 0:
        print ("fizz")

    #check if count is a multiple of 5. If so, print buzz
    elif count % 5 == 0:
        print ("buzz")

    #otherwise print the number
    else:
        print count
