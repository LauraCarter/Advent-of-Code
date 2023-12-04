import re

with open("231204 input.txt", "r") as input:

    # import text file
    file = input.readlines()

    total = 0

    # set up a list where each item is a list of two elements: the number of copies and the number of points
    cardcopies = []

    for j in file:

        card = j.split(": ")
        #print(card)

        # work out the number of points for each copy of the card
        nums = card[1].split(" | ")
        #print(nums)

        winlist = nums[0].split()
        winset = set(winlist)
        #print(winlist)
        #print(winset)

        havelist = nums[1].split()
        haveset = set(havelist)
        #print(havelist)
        #print(haveset)

        actualwins = winset.intersection(haveset)
        #print(actualwins)

        cardwins = len(actualwins)
        #print(cardwins)

        if actualwins != set():
            points = 2**(cardwins-1)
            # print(points,"points")
            total = total+points
        else:
            points = 0

        cardentry = [1]
        cardentry.append(cardwins)

        cardcopies.append(cardentry)
        
    #print("total points:", total)


    k = 0
    cardtotal = 0

    for j in cardcopies:

        extras = j[1] #number of extra cards
        # print(extras)

        a = 0

        while ( a < extras ) and ( a + k < 186 ):

            cardcopies[k+a+1][0] = cardcopies[k+a+1][0]+cardcopies[k][0]

            a = a+1

        k=k+1

        cardtotal = cardtotal + j[0]


    print(cardcopies) # array of single copies of cards and their points values
    print(cardtotal)

input.close()