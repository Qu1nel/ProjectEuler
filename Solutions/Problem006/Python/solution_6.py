"""Compute the square of the sum minus the sum of the squares."""


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
