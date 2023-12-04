import re

with open("231204 input.txt", "r") as input:

    # import text file
    file = input.readlines()

    total = 0

    for j in file:

        card = j.split(": ")
        #print(card)

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

    print("total points:", total)

input.close()