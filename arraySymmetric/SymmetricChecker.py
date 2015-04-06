__author__ = 'markchan'


def symmetric_check(myList):
    size = len(myList)

    for i in range(size):
        for j in range(size):
            if myList[i][j] != myList[j][i]:
                return False

    return True


print symmetric_check([[1, 2, 3],
                       [2, 3, 4],
                       [3, 3, 1]])

