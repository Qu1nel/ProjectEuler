"""2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""


class Solution:
    def __init__(self):
        self.start = 1
        self.end = 20
        self.numbers = [num for num in range(self.start, self.end + 1)]

    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def calculate_answer(self) -> int:
        result = self.numbers[0]

        for i in range(self.end):
            result = self.numbers[i] * int(result / self.gcd(self.numbers[i], result))

        return result


def main() -> None:
    runner = Solution()
    result = runner.calculate_answer()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

