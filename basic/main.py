import math


def fib(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    else: return fib(n - 1) + fib(n - 2)


def binary(n):
    return int(bin(n)[2:])


def Hex(n):
    return "{0:x}".format(n)


def Sum_n(n):
    s = 0
    while (n != 0):
        s += n % 10
        n = n // 10
    return s


def convert_ascii(s):
    return [ord(c) for c in s]


def Check_prime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0: return False
        return True
    return False


def Print(n):
    i = 2
    while (n > 1):
        if (Check_prime(i)):
            if n % i == 0:
                print(i,end = ".")
                n = n / i
            else:
                i = i + 1
        else:
            i = i + 1


Print(28)
