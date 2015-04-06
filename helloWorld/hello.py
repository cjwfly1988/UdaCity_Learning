__author__ = 'markchan'
name = 'my things'

s = 'anystring'
# print s
# print s[:3] + s[3:]
# if the target string is not found, return -1

sentence = 'this is from the future world'
word = 'hello'

# print word.find('hello')

# print sentence.find('from', 10)  # start searching from position 10

# print sentence[8:]


def sum(a, b):
    a = a + b
    return a


def find_second(target, search):
    first_occurence = target.find(search)
    print first_occurence

    second_occurence = target.find(search, first_occurence + 1)

    return second_occurence


def is_friend(friend_name):
    if friend_name[0] == "D" or friend_name[0] == "N":
        return True


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


print bigger(1, 3)


def biggest(a, b, c):
    return bigger(bigger(a, b), c)


print biggest(20, 3, 4)


def factorial(n):
    i = 1
    while n >= 1:
        i = i * n
        n = n - 1
    return i


def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print ('blast off')


def find_last(target, search):
    last_pos = -1
    while True:
        position = target.find(search, last_pos + 1)
        if position == -1:
            return last_pos
        else:
            last_pos = position


# print factorial(5)
print countdown(5)

print find_last("11111111", '1')