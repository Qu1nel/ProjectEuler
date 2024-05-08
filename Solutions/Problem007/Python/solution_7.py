"""By listing the first six prime numbers:

2, 3, 5, 7, 11 and 13, we can see that the 6-th prime is 13.

What is the 10,001-st prime number?
"""

import math


class Solution:
    def __init__(self):
        self.n = 10001

    def is_prime(self, a: int) -> bool:
        if a <= 3:
            return a > 1

        if a % 2 == 0 or a % 3 == 0:
            return False

        for i in range(5, int(math.sqrt(a)) + 1, 6):
            if a % i == 0 or a % (i + 2) == 0:
                return False

        return True

    def calculate_answer(self) -> int:
        number_check = 2
        i = 1

        while i != self.n:
            number_check += 1
            if self.is_prime(number_check):
                i += 1

        return number_check


def main() -> None:
    runner = Solution()
    result = runner.calculate_answer()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
