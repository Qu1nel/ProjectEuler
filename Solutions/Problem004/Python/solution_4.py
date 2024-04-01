"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


class Solution:
    def is_palindrome(self, num):
        if num <= 0:
            return num == 0

        reverse_num = 0
        saved_num = num

        while num > 0:
            reverse_num = reverse_num * 10 + num % 10
            num //= 10

        return reverse_num == saved_num


    def calculate_answer(self):
        large_number = -1
        for a in range(999, 99, -1):
            for b in range(999, 99, -1):
                num = a * b
                if self.is_palindrome(num) and num > large_number:
                    large_number = num
        return large_number


def main() -> None:
    runner = Solution()
    result = runner.calculate_answer()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

