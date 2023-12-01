with open("231201 input.txt", "r") as input:
    # import text file
    list = input.readlines()

    # new list for counting
    calib = []

    # converting each string into a calibration value
    for i in list:

        x = i
        # print(x)

        y = x.strip("abcdefghijklmnopqrstuvwxyz\n")
        # print(y)

        a = y[0]
        b = y[-1]
        c = a+b
        d = int(c)
        # print(d)
        calib.append(d)
    
    print(calib)

    # adding up all the values
    total = 0

    for j in calib:
        total = total + j

    print(total)

input.close()
