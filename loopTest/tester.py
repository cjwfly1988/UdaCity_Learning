__author__ = 'markchan'

list_01 = [1, 2, 3, 4]
list_02 = [1, 2, 3, 4]
list_03 = [1, 2, 3, 4]

list_01 = list_01 + [5]
list_02.append(5)

print 'this is list 01 first time', list_01
print 'this is list 02 first time', list_02
print 'this is list 03 first time', list_03


def proc(mylist):
    mylist = mylist + [9]


def proc2(mylist):
    mylist.append(6)


def proc3(mylist):
    mylist += [5]


print '******************************'
proc(list_01)
print 'this is list 01 second time', list_01

proc2(list_02)
print  'this is list 02 second time', list_02

proc3(list_03)
print 'this is list 03 second time', list_03

list_01 = list_01 + [7, 8, 9]
print list_01

