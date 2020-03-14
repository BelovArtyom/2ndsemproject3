import timeit

# work function for recursion
def findindrecb(numlist, num, ind):
    if num == numlist[ind]:
        return ind
    # if not the needed one
    if ind != len(numlist) - 1:
        return findindrecb(numlist, num, ind + 1)
    # after trying all the indexes
    else:
        return None


# call function for recursion
def findindrec(numlist, num):
    num = int(num)
    return findindrecb(numlist, num, 0)


# non-recursive function
def findind(numlist, num):
    num = int(num)
    for x in range(0, len(numlist)):
        if num == numlist[x]:
            return x
    # if algorithm doesn't find a single number it gets here
    return None


listofnum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]


timeit.timeit('findind(listofnum, 6)', number=10000)

timeit.timeit('findindrec(listofnum, 6)', number=10000)


'''
print(findind(listofnum, 8), 'nonrec')
print(findindrec(listofnum, 8), 'rec')
'''
