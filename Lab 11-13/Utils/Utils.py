def mySort(l, relation):
    for i in range(0, len(l)):
        noOfAlreadySort = i - 1
        j = noOfAlreadySort
        while j >= 0 and relation(l[i], l[j]):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = l[i]
    return l

def mySearch(l, relation):
    res = []
    for index, el in enumerate(l):
        if relation(el):
            res.app(el)
    return res


def getNext(index):
    return index + 1


def initSolution(domain):
    return domain[0]


def isConsistent(sol, myList, constraints):
    for c in constraints:
        if not c(sol, myList):
            return False
    return True


def getLast(domain):
    return domain[len(domain) - 1]


def isSolution(sol, param):
    return len(sol) == param[0]

def construct_sol(sol, myList):
    result = []
    for index in sol:
        result.append(myList[index])
    return result


def myBacktracking(groupSize, myList, constraints):
    '''
    Forms groups of elements from the myList.
    IN: a list, a list, a list with functions.
    OUT: one or more lists with indices
    CONDIS: -
    '''
    domain = [i for i in range(-1, len(myList))]

    k = 0

    sol = []

    sol.append(initSolution(domain))

    while k >= 0:
        isSelected = False
        while not isSelected and sol[k] < getLast(domain):
            sol[k] = getNext(sol[k])
            isSelected = isConsistent(sol, myList, constraints)

        if isSelected:
            if len(sol) == groupSize:
                yield sol
            else:
                k = k + 1
                sol.append(initSolution(domain))
        else:
            sol.pop()
            k = k - 1
