import re

with open("231201 input.txt", "r") as input:
    # import text file
    list = input.readlines()

    # new list for counting
    calib = []

    # converting each string into a calibration value
    for x in list:
        print(x)
        y = re.findall("(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))", x)
        print(y)

        a = y[0]
        b = y[-1]

        print(a)
        print(b)
    
        a=a.replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
        b=b.replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
        print(a)
        print(b)

        c = a+b
        d = int(c)
        print(d)
    
        calib.append(d)
    
    print(calib)

    # adding up all the values
    total = 0

    for j in calib:
        total = total + j

    print(total)

input.close()