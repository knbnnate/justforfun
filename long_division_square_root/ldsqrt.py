def ldsqrt(instring):
    instring = str(instring)
    dots = instring.count(".")
    assert dots in [0, 1]
    if dots == 0:
        instring = instring+".00"
    stringparts = instring.partition(".")
    leftstring = stringparts[0]
    if len(leftstring) == 0:
      leftstring = "00"
    assert leftstring.isnumeric()
    rightstring = stringparts[2]
    assert rightstring.isnumeric()
    leftstringrightdigits = leftstring[::-2]
    leftstringleftdigits = leftstring[0:-1][::-2]
    leftstringpairs = []
    for i in range(len(leftstringrightdigits)):
        if i < len(leftstringleftdigits):
            leftstringpairs.append(
                (int(leftstringleftdigits[i]), int(leftstringrightdigits[i])))
        else:
            leftstringpairs.append((0, int(leftstringrightdigits[i])))
    leftstringpairs = leftstringpairs[::-1]
    rightstringleftdigits = rightstring[::2]
    rightstringrightdigits = rightstring[1:][::2]
    rightstringpairs = []
    for i in range(len(rightstringleftdigits)):
        if i < len(rightstringrightdigits):
            rightstringpairs.append(
                (int(rightstringleftdigits[i]), int(rightstringrightdigits[i])))
        else:
            rightstringpairs.append((int(rightstringleftdigits[i]), 0))
    topleft = []
    topright = []
    currentside = "left"
    currentpairs = leftstringpairs
    currenttop = topleft

    def pairparse(intup):
        return "{}{}".format(intup[0], intup[1])

    dots = None
    instring = None
    leftstring = None
    leftstringleftdigits = None
    leftstringrightdigits = None
    rightstring = None
    rightstringleftdigits = None
    rightstringrightdigits = None
    stringparts = None
    seedpair = 10*leftstringpairs[0][0]+leftstringpairs[0][1]
    if seedpair == 0:
        seedroot = 0
    elif seedpair < 4:
        seedroot = 1
    elif seedpair < 9:
        seedroot = 2
    elif seedpair < 16:
        seedroot = 3
    elif seedpair < 25:
        seedroot = 4
    elif seedpair < 36:
        seedroot = 5
    elif seedpair < 49:
        seedroot = 6
    elif seedpair < 63:
        seedroot = 7
    elif seedpair < 81:
        seedroot = 8
    elif seedpair < 100:
        seedroot = 9
    topleft.append(str(seedroot))
    if len(currentpairs) > 1:
        nextseedpair = 10*currentpairs[1][0]+currentpairs[1][1]
    else:
        currentpairs = rightstringpairs
        currentside = "right"
        currenttop = topright
        nextseedpair = 10*currentpairs[0][0] + \
            currentpairs[0][1]
    outeronesdigit = seedroot
    outersignificance = 10
    outersignificantdigits = outersignificance * \
        (seedroot+seedroot)
    inneroperand = 100*(seedpair-seedroot*seedroot)+nextseedpair
    testproduct = inneroperand+1
    candidate = 9
    while testproduct > inneroperand:
        outervalue = outersignificantdigits+candidate
        testproduct = outervalue * candidate
        if testproduct > inneroperand:
            candidate = candidate-1
    currenttop.append(str(candidate))
    nextpairindex = 1
    while nextseedpair is not None:
        if currentside == "left":
            if nextpairindex+1 < len(currentpairs):
                nextpairindex = nextpairindex+1
                nextseedpair = 10 * \
                    currentpairs[nextpairindex][0] + \
                    currentpairs[nextpairindex][1]
            else:
                currentpairs = rightstringpairs
                currentside = "right"
                currenttop = topright
                nextpairindex = 0
                nextseedpair = 10*currentpairs[0][0]+currentpairs[0][1]
        else:
            if nextpairindex+1 < len(currentpairs):
                nextpairindex = nextpairindex+1
                nextseedpair = 10 * \
                    currentpairs[nextpairindex][0] + \
                    currentpairs[nextpairindex][1]
            else:
                nextseedpair = None
        if nextseedpair is not None:
            inneroperand = 100*(inneroperand-testproduct)+nextseedpair
            outersignificantdigits = outervalue + candidate  # 49 + 9 is 58
            testproduct = inneroperand+1
            candidate = 9
            while testproduct > inneroperand:
                outervalue = outersignificance*outersignificantdigits+candidate
                testproduct = outervalue * candidate
                if testproduct > inneroperand:
                    candidate = candidate-1
            currenttop.append(str(candidate))
    if "".join(topright).replace("0","") == "":
      topright=[]
      dot=""
    else:
      dot="."
    return "{}{}{}".format("".join(topleft), dot, "".join(topright))

#print(ldsqrt(".01"))