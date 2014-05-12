from time import gmtime, strftime
import sys

def get(c):
    return strftime("%" + c)

def getTimeArray():
    return [get("H"), get("M"), get("S")]

def getDateArray():
    return [get("Y"), get("m"), get("d")]

def getTimeString():
    timeA = getTimeArray()
    return timeA[0]+" "+timeA[1]+" "+timeA[2]

def logTime():
    str = sys.argv[1]
    print str
    if str != "riley" and str != "brent":
        print str + " is not riley"
        print "invalid user, goodbye"
        exit(1)

    if sys.argv[2] != "in" and sys.argv[2] != "out":
        "wrong in or out input."
        exit(1)

    str += " " + sys.argv[2] + ": " + strftime("%Y-%m-%d %H:%M:%S")   

    with open("clock.txt", "a") as clock:
        clock.write(str + "\n");

    print"logged " + str

if len(sys.argv) == 3:
    logTime()
