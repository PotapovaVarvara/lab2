def ex_1():
    n = input("Enter n: ")
    m = input("Enter m: ")
    k = input("Enter k: ")
    if n > m and n > k:
        print("Max is n")
    if m > n and m > k:
        print("Max is m")
    if k > n and k > m:
        print("Max is k")


def ex_2():
    n = input("Enter n: ")
    m = input("Enter m: ")
    print("Odd numbers between: ")
    _get_odd_between(int(n), int(m))


def _get_odd_between(min_, max_):
    i = min_ + 1
    while i < max_:
        isOdd = i % 2 != 0
        if isOdd:
            print(str(i))
        i = i+1


def ex_3():
    age = input("Enter your age: ")
    _get_if_old(int(age))


def _get_if_old(age):
    if age > 18:
        print("Old enough")
    else:
        print("Not old enough")


def ex_4():
    i1 = input("Enter first integer: ")
    i2 = input("Enter second integer: ")
    operation = input("Enter operation - A-Add, S-Subtraction: ")
    print("Result: ")
    _execute_operation(i1, i2, operation);


def _execute_operation(integer1, integer2, operation):
    if operation == "A":
        print(int(integer1)+int(integer2))
    if operation == "S":
        print(int(integer1)-int(integer2))



ex_4()
