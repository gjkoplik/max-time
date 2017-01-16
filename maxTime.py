# Gary Koplik
# Spring, 2017
# maxTime.py

from itertools import permutations as perm # to permute the input list
import sys # to input the integers when running the code

# takes 4 integers inputted on the command line when running code: a, b, c, d
# finds highest possible time value or returns 'not possible'
#   Note: time is military time i.e. bounded between [00:00, 24:00]
def maxTime(a, b, c, d):
    # put integers into list
    timeList = [a, b, c, d]

    # create list of all permuations (each is a tuple) of elements in timeList
    permuted = list(perm(timeList))

    # turn each tuple in timeList into string
    for i in range(len(permuted) - 1):
        permuted[i] = ''.join(permuted[i])

    # only save plausible times in to new list
    goodList = []
    for i in range(len(permuted) - 1):
        # keep values <= 2400 and last two digits <= 60
        if int(permuted[i]) <= 2400 and int(permuted[i][2:]) <= 60:
            goodList.append(permuted[i])

    # if this new list is empty => no possible answer
    if len(goodList) == 0:
        return 'not possible'

    # convert all strings into integers (so we can sort them)
    goodList = map(int, goodList)

    # sort in ascending order, convert back to strings (for outputting in time form)
    #   then grab last (i.e. largest) term
    answer = str(sorted(goodList)[-1])

    # one issue to resolve, lots of zero values
    # for example, suppose you input 5 0 0 0
    #   then the max time is 05:00, but when converted to int earlier
    #       0500 became 500
    # this only happens when the first terms are 0, so this is an easy fix
    # append 0s onto the front of the answer until it is length 4
    while len(answer) != 4:
        answer = '0' + answer

    # return in time form
    answerAsTime = answer[0:2] + ':' + answer[2:]
    return answerAsTime

if __name__ == "__main__":
    final = maxTime(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print final
