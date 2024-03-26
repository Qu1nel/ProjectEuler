"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

class Solution:

    @staticmethod
    def calculate_answer() -> int:
        summ = 0
        num = 1

        while num < 1000:
            summ += num if num % 3 == 0 or num % 5 == 0 else 0
            num += 1

        return summ


def main() -> None:
    runner = Solution()
    result = runner.calculate_answer()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

