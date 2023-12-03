import re

with open("231203 input.txt", "r") as input:

    # import text file
    file = input.readlines()
    
    part1answer = 0
    t=0
    j=0

    gearsum = 0

    for y in file:

        #y = file[j]
        #print(y)

        i = 0
        length = len(y)



        while i < length:
            
            # find possible gears
            if y[i] == '*':
                print('possible gear at',i)

                topline = file[j-1][i-3:i+4]
                midline = file[j][i-3:i+4]
                botline = file[j+1][i-3:i+4]
                print(topline)
                print(midline)
                print(botline,'\n')

                # find all the part numbers in this grid

                value = ''
                pos = 0 #position counter
                toplocs = set()  # set of locations of digits
                tester = set()

                gearvaluelist = [] # lists all the values around this gear

                for k in topline:

                    topgood = {2,3,4}

                    if re.findall("\d", k):
                        value = value+k     # concatenating actual digits
                        toplocs.add(pos)

                    else:
                        if value != '': 
                            print(value)    # returning only actual numbers (in string form)
                            print(toplocs)

                            tester = topgood.intersection(toplocs)
                            print(tester)
                            if tester != set():
                                gearvaluelist.append(value)
                                print ('added gear with value',value)
                            tester = set()
                                
                        value = ''
                        toplocs = set() #

                    pos = pos+1

                tester = topgood.intersection(toplocs)
                print(tester)
                if tester != set():
                    gearvaluelist.append(value)
                    print ('added gear with value',value)
                    tester = set()

                value = ''
                pos = 0 #position counter
                midlocs = set()  # set of locations of digits
                tester = set()

                for m in midline:

                    midgood = {2,4}

                    if re.findall("\d", m):
                        value = value+m     # concatenating actual digits
                        midlocs.add(pos)
                        

                    else:
                        if value != '': 
                            print(value)    # returning only actual numbers (in string form)
                            print(midlocs)

                            tester = midgood.intersection(midlocs)
                            print(tester)
                            if tester != set():
                                gearvaluelist.append(value)
                                print ('added gear with value',value)
                                tester = set()

                            value = ''
                            midlocs = set()
                    
                    pos = pos+1

                tester = midgood.intersection(midlocs)
                print(tester)
                if tester != set():
                    gearvaluelist.append(value)
                    print ('added gear with value',value)      
                    tester = set()     

                value = ''
                pos = 0
                botlocs = set()
                tester = set()

                for k in botline:

                    botgood = {2,3,4}

                    if re.findall("\d", k):
                        value = value+k     # concatenating actual digits
                        botlocs.add(pos)

                    else:
                        if value != '': 
                            print(value)    # returning only actual numbers (in string form)
                            print(botlocs)
                            print(tester)

                            tester = botgood.intersection(botlocs)
                            if tester != set():
                                gearvaluelist.append(value)
                                print ('added gear with value',value)
                            tester = set()

                        
                        value = ''
                        botlocs = set()
                    
                    
                    pos = pos+1

                tester = botgood.intersection(botlocs)
                if tester != set():
                    gearvaluelist.append(value)
                    print ('added gear with value',value)
                    tester = set()

                print(gearvaluelist,'is the list of gears')

                if len(gearvaluelist) == 2:
                    gearprod = int(gearvaluelist[0])*int(gearvaluelist[1])
                    print('product of gears',gearprod)
                    gearsum = gearsum + gearprod


            i = i+1

        j = j+1

    print('sum of products',gearsum)

input.close()