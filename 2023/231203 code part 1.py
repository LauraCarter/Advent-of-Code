import re

with open("231203 input.txt", "r") as input:

    # import text file
    file = input.readlines()
    
    part1answer = 0
    t=0

    for y in file:

        value = ''
        numSurround = {}
        checker = {'0','1','2','3','4','5','6','7','8','9','\n','.'}

        pos = 0

        for i in y:

            if re.findall("\d", i):
                value = value+i     # concatenating actual digits

            # check if there is a symbol around the digit

                if t == 0:
                    digitSurround = {y[pos-1], y[pos+1],file[t+1][pos-1], file[t+1][pos], file[t+1][pos+1]}
                else: 
                    if t == len(file)-1:
                        digitSurround = {y[pos-1], y[pos+1],file[t-1][pos-1], file[t-1][pos], file[t-1][pos+1]}
                    else:
                        digitSurround = {y[pos-1], y[pos+1],file[t-1][pos-1], file[t-1][pos], file[t-1][pos+1], file[t+1][pos-1], file[t+1][pos], file[t+1][pos+1]}

                numSurround = digitSurround.union(numSurround)

            else:
                if value != '': 
                    print(numSurround)
                    tester = numSurround.difference(checker)
                    print(tester)
                    print(value)    # returning only actual numbers (in string form)

                    if tester != set():
                        part1answer = part1answer + int(value)
                        print(part1answer)
            
                value = ''
                numSurround = {}

            pos = pos+1

        t = t+1

    print(part1answer)

input.close()