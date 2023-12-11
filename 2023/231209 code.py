import re

with open("231209 input.txt", "r") as input:

    # import text file
    file = input.readlines()

    #print(file)
    #print(len(file))

    total = 0

    f = 0
    while f < len(file):

        sequence = file[f].split()
        #print(sequence)

        s = 0
        while s < len(sequence):
            sequence[s] = int(sequence[s])
            s=s+1
        #print(sequence)

        seqlength = len(sequence)
        #print(seqlength)

        # set up a list of the differences in the triangle form
        triangle = []
        triangle.append(sequence)

        q = 0

        while q < seqlength-1:
            rowdiffs = []
            j = 1
            while j < seqlength - q:
                diff = triangle[q][j]-triangle[q][j-1]
                rowdiffs.append(diff)
                
                j=j+1

            #print(rowdiffs)
            triangle.append(rowdiffs)
            q=q+1

        #print(triangle)
        #print(len(triangle))

        revq = 1

        while revq < seqlength:
            #print(triangle[seqlength-revq-1])
            differ = triangle[seqlength-revq][-1]
            last = triangle[seqlength-revq-1][-1]
            #print(differ, last)
            triangle[seqlength-revq-1].append(differ+last)
            #print(triangle[seqlength-revq-1])
            revq = revq+1

        newvalue = triangle[0][-1]
        total=total+newvalue

        f=f+1
    
    print("part 1 answer:", total)

    f = 0
    total = 0
    
    #reverse version
    while f < len(file):

        sequence = file[f].split()
        sequence.reverse()
        #print(sequence)

        s = 0
        while s < len(sequence):
            sequence[s] = int(sequence[s])
            s=s+1
        #print(sequence)

        seqlength = len(sequence)
        #print(seqlength)

        # set up a list of the differences in the triangle form
        triangle = []
        triangle.append(sequence)

        q = 0

        while q < seqlength-1:
            rowdiffs = []
            j = 1
            while j < seqlength - q:
                diff = triangle[q][j]-triangle[q][j-1]
                rowdiffs.append(diff)
                
                j=j+1

            #print(rowdiffs)
            triangle.append(rowdiffs)
            q=q+1

        #print(triangle)
        #print(len(triangle))

        revq = 1

        while revq < seqlength:
            #print(triangle[seqlength-revq-1])
            differ = triangle[seqlength-revq][-1]
            last = triangle[seqlength-revq-1][-1]
            #print(differ, last)
            triangle[seqlength-revq-1].append(differ+last)
            #print(triangle[seqlength-revq-1])
            revq = revq+1

        newvalue = triangle[0][-1]
        total=total+newvalue

        f=f+1
    
    print("part 2 answer:", total)



input.close()
