t = int(input())
while(t):
    usrYear = int(input())

    diffYear = usrYear - 2001
    leapYear = diffYear // 4
    normalYear = diffYear - leapYear

    totalIncriment = 2 * leapYear + normalYear

    theDay = abs(totalIncriment) % 7

    dict = {0: "Monday", 1: "Tuesday", 2: "wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    #
    # print("The input Year is ", usrYear)
    # print("The diffrance of Year is ", diffYear)
    # print("The the number of leap Year is ", leapYear)
    # print("The number of normal Year is ", normalYear)
    # print("The total incriemnt is ", totalIncriment)

    if (usrYear <= 2001):
        print(dict[7 - theDay])
    else:
        print(dict[theDay])
    t -= 1
