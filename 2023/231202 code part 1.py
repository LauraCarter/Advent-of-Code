import re

with open("231202 input.txt", "r") as input:
    # import text file
    list = input.readlines()
    #print(list)

    idsum = 0 #sum for all the IDs

    for x in list: 

        print(x)


        # split into game numbers and results
        y = x.split(": ")
        print(y)

       # find number of game
        p = y[0]
        q = p.strip("Game ")
        gamenum = int(q)
        print(gamenum)

        # split results by drawings
        z = y[1].split("; ")
        print(z) # list where each item is a drawing

        failcount = 0 # counter for impossible drawings

    # split drawings by colour
        for i in z:
            draw = i.split(", ")
            print(draw) # list where each item is a colour

        
            for j in draw:

            # look for impossible colour drawings i.e. red more than 12
                red = re.search('red',j)
                if red:
                    print('red')
                    a = j.split(" ")
                    print(a)
                    b = int(a[0])
                    print(b)
                    if b > 12:
                        print('redfail')
                        failcount = failcount+1
                 
                green = re.search('green',j)
                if green:
                    print('green')
                    a = j.split(" ")
                    print(a)
                    b = int(a[0])
                    print(b)
                    if b > 13:
                        print('greenfail')
                        failcount = failcount+1

                blue = re.search('blue',j)
                if blue:
                    print('blue')
                    a = j.split(" ")
                    print(a)
                    b = int(a[0])
                    print(b)
                    if b > 14:
                        print('bluefail')
                        failcount = failcount+1

        print('fails =',failcount)
        if failcount == 0:
            idsum = idsum + gamenum

print("total =",idsum)
            


input.close()