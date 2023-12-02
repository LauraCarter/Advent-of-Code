import re

with open("231202 input.txt", "r") as input:
    # import text file
    list = input.readlines()
    #print(list)

    powersum = 0 #sum for all the powers

    for x in list: 

        print(x)

        # split into all drawings
        y = x.split(": ")
        print(y)

        # split results by drawings
        z = y[1].split("; ")
        print(z) # list where each item is a drawing

        failcount = 0 # counter for impossible drawings

        redlist = []
        greenlist = []
        bluelist = []

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
                    redlist.append(b)

                 
                green = re.search('green',j)
                if green:
                    print('green')
                    a = j.split(" ")
                    print(a)
                    b = int(a[0])
                    print(b)
                    bluelist.append(b)

                blue = re.search('blue',j)
                if blue:
                    print('blue')
                    a = j.split(" ")
                    print(a)
                    b = int(a[0])
                    print(b)
                    greenlist.append(b)

            print('reds ',redlist)
            print('blues ',bluelist)          
            print('greens ',greenlist)

        redmax=max(redlist)
        bluemax=max(bluelist)
        greenmax=max(greenlist)

        print("max red ", redmax)
        print("max blue ", bluemax)
        print("max green ", greenmax)

        power=redmax*bluemax*greenmax

        powersum = powersum+power

print("total =",powersum)
            


input.close()