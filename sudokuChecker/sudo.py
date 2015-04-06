__author__ = 'markchan'


def check_sudo(sudo):
    size = len(sudo)
    digit = 1
    while digit <= size:
        i = 0
        while i < size:
            row_count = 0
            col_count = 0
            j = 0
            while j < size:
                if sudo[i][j] == digit:
                    row_count += 1
                if sudo[j][i] == digit:
                    col_count += 1

                j = j + 1

            if row_count != 1 and col_count != 1:
                return False

            i = i + 1
            digit = digit + 1

    return True


xman = [[1, 2, 3],
        [2, 3, 1],
        [3, 1, 2]]

evil = [[1, 2, 3, 4],
        [2, 3, 1, 3],
        [3, 1, 2, 3],
        [4, 4, 4, 4]]

print len(xman)

print check_sudo(xman)
print check_sudo(evil)

