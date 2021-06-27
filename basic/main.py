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


print(convert_ascii("aa"))
