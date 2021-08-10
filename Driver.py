import time

from Number import Number


def odd(n):
    return (3 * int(n)) + 1


def even(n):
    return int(n) / 2


def complete_pass(n):
    num_object = Number(n)
    while n > 1:
        if n % 2 == 0:
            n = even(n)
        else:
            n = odd(n)
        num_object.append_iteration()
        num_object.add_visit(n)
    print(num_object)


class Driver:
    startTime = time.time()
    count = 2

    #currentNumber = input("Press enter to make passes up to 1000 ")

    while count <= 100:
        complete_pass(count)
        count += 1

    print(time.time() - startTime)
