# 6. Sum Square Difference

## Problem

For the integers from 1 through `n`, subtract the sum of their squares from the square of their sum. [Project Euler asks for the result when `n = 100`](https://projecteuler.net/problem=6).

## Idea

Let $S_1 = \sum_{k=1}^{n}k$ and $S_2 = \sum_{k=1}^{n}k^2$. Pairing the sum with its reverse gives $2S_1 = n(n+1)$, so $S_1 = n(n+1)/2$.

To find $S_2$, sum the identity $(k+1)^3-k^3 = 3k^2+3k+1$ from $k=1$ through $n$. The intermediate cubes cancel, giving $(n+1)^3-1 = 3S_2+3S_1+n$. Substituting $S_1$ and solving for $S_2$ gives $S_2 = n(n+1)(2n+1)/6$.

Substitute both sums into the requested difference. The last line is the integer formula used in the code.

$$
\begin{aligned}
S_1^2-S_2
  &= \frac{n^2(n+1)^2}{4} - \frac{n(n+1)(2n+1)}{6} \\
  &= \frac{3n^4+2n^3-3n^2-2n}{12}.
\end{aligned}
$$

## Complexity

The formula uses a constant number of arithmetic operations and intermediate integers. With Python's arbitrary-precision integers, those integers use $O(\log n)$ bits.

## Example

For `n = 10`, the sum is `55` and the sum of the squares is `385`. Squaring the first sum and subtracting the second gives `55² − 385 = 2640`.

[Python solution](Python/solution_6.py)
