import re
import pandas as pd
import numpy as np


def main():
    data = "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Scott555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
    # Part 1: Extract numbers, using findall function to just pull out anything that has numbers
    # [\(\d\)]* is to grab any area codes if included,
    # [-\s] is the grab any hyphens or spaces if included,
    # \d* is used to grab any numbers after an area code if given or starts the numbers before another hypen appears
    # \d+ grabs the final part of the number which is always there, hence why it is given the '+'
    data_p1 = re.findall('[\(\d\)]*[-\s]*\d*[-\s]*\d+', data)
    print(data_p1, "\n")

    # Part 2: Extract Names
    data_p2 = re.findall('[a-zA-Z\.]*[\,\.\s]*[a-zA-Z]+[\,\.\s]*[a-zA-Z]*[\,\.\s]*[a-zA-Z]+', data)
    print(data_p2, "\n")

    # Part 3:
    data_p3 = data_p2
    for x in range(len(data_p3)):
        if re.findall(',', data_p3[x]):
            g1 = re.split(", " or ". ", data_p3[x])
            data_p3[x] = g1[1] + " " + g1[0]
            re.sub(",", " ", data_p3[x])

    print(data_p3, "\n")

    # Part 4:
    data_p4 = pd.Series(data_p3)
    data_p4_1 = data_p4.str.contains("\.")
    print(data_p4_1, "\n")

    # Part 5 (commented out because it is incomplete):
    # data_p5 = pd.Series(data_p3)
    # for x in data_p5[x]:
    #    if x.str.contains("\."):
    #        
    # data_p5_1 = 1
    # print(data_p5.str.contains("\."), "\n")

    # Part 6:
    data_p6 = "<title>+++BREAKING NEWS+++<title>"
    # The regex below matches the entire string because a period without a backslash represents a wildcard,
    # the period by itself matches any single character, adding a plus makes it grab anything between '<' and '>'
    # the fix is given in the code that is not commented below
    # d6 = re.findall("<.+>", data_p6)
    # print(d6, "\n")
    d6 = re.search("<title>", data_p6)[0]
    print(d6, "\n")

    # Part 7:
    data_p7 = "(5-3)^2=5^2-2*5*3+3^2"
    # The regex below matches only '-' because of the ^ within the brackets
    # '^' will look not match with anything in the given set, '-' is the match that it gives
    # The fix is given in the code that is not commented below (lazy fix as the problem asks for it all to be included)
    # d7 = re.search("[^0-9=+*()]+", data_p7)[0]
    d7 = re.findall("[\S]+", data_p7)[0]
    print(d7)


if __name__ == "__main__":
    main()
