"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

from math import sqrt
from random import randint


class Solution:
    number: int

    def __init__(self) -> None:
        self.number = 600851475143

    def miller_rabin_test(self, d: int, number: int) -> bool:
        a = 2 + randint(1, number - 4)
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


    def is_prime(self, number: int, k: int) -> bool:
        if number < 2 or number == 4:
            return False
        if number <= 3:
            return True

        d = number - 1
        while d % 2 == 0:
            d //= 2

        for _ in range(1, k):
            if self.miller_rabin_test(d, number) is False:
                return False

        return True


    def calculate_answer(self) -> int:
        large_factory = 1
        for n in range(2, int(sqrt(self.number)) + 1):
            if self.number % n == 0 and self.is_prime(n, k=4) and large_factory < n:
                large_factory = n

        return large_factory


def main() -> None:
    runner = Solution()
    result = runner.calculate_answer()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

