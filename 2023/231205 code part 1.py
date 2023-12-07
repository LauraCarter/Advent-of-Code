import re

with open("231205 input.txt", "r") as input:

    # import text file
    file = input.readlines()

    # create a list of seeds
    firstline = file[0]
    seedline = firstline.split(':')  
    seedlist = seedline[1].split()
    # print(seedlist)

    # create a list of where seeds end up
    seedend = []

    maplist = []
    ind = 0

    # create list of maps and their indices
    for x in file:
        if re.findall("[map]", x):
            new = [x, ind]
            maplist.append(new)
        ind = ind+1

    maplist.append(['done', ind]) # have a marker for the end (may not need this)

    # create a list where each item is the list of a particular map
    maps = []
    k=0
    while k < len(maplist)-1:
        maps.append(file[maplist[k][1]+1:maplist[k+1][1]])
        k = k+1
    #print(maps)

    # running for each seed
    j = 0
    while j < len(seedlist):

        testseed = int(seedlist[j])
        print(testseed)

        m = 0

        while m < len(maps):
            mapping = maps[m][0:-1]
            print(mapping)

            for q in mapping:

                coords = q.split()
                print(coords)
                deststart = int(coords[0])
                sourcestart = int(coords[1])
                range = int(coords[2])

                if (testseed >= sourcestart) and (testseed < sourcestart+range):
                    testseed = testseed + deststart - sourcestart
                    print(testseed)
                    
                    break
            


            m = m+1

        seedend.append(testseed)

        j = j+1

    print(seedend)
                
    nearest = min(seedend)
    print ("nearest seed at",nearest)

input.close()