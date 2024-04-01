import random
from math import sqrt


def miller_rabin_test(d: int, number: int) -> bool:
    a = 2 + random.randint(1, number - 4)
    x = pow(a, d, number)

    if x in (1, number - 1):
        return True

    while d != number - 1:
        x = (x * x) % number
        d *= 2

        if x == 1:
            return False
        if x == number - 1:
            return True

    return False


def is_prime(number: int) -> bool:
    k = 4
    if number < 2 or number == 4:
        return False
    if number <= 3:
        return True

    d = number - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(1, k):
        if miller_rabin_test(d, number) is False:
            return False

    return True


def test(num):
    result = []
    factors = []
    for n in range(2, int(sqrt(num) + 1)):
        if num % n == 0:
            result.append(n)
            if is_prime(n):
                factors.append(n)
    return result, factors

