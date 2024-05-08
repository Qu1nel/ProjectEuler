"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^3 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


class Solution:
    def __init__(self):
        self.n = 100

    def calculate_answer(self) -> int:
        result = (3 * self.n**4 + 2 * self.n**3 - 3 * self.n**2 - 2 * self.n) // 12
        return result


def main() -> None:
    runner = Solution()
    result = runner.calculate_answer()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
