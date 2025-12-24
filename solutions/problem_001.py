"""
Project Euler - Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solve(limit=1000):
    """
    Calculate the sum of all multiples of 3 or 5 below the given limit.
    
    Args:
        limit: The upper bound (exclusive) for finding multiples
        
    Returns:
        The sum of all multiples of 3 or 5 below limit
    """
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def solve_optimized(limit=1000):
    """
    Optimized solution using arithmetic series formula.
    
    Sum of multiples of n below limit = n * (1 + 2 + ... + k) where k = (limit-1)//n
    Using formula: sum = n * k * (k + 1) / 2
    """
    def sum_divisible_by(n, limit):
        k = (limit - 1) // n
        return n * k * (k + 1) // 2
    
    # Sum of multiples of 3 + multiples of 5 - multiples of 15 (to avoid double counting)
    return sum_divisible_by(3, limit) + sum_divisible_by(5, limit) - sum_divisible_by(15, limit)


if __name__ == "__main__":
    result = solve()
    print(f"Solution (basic): {result}")
    
    result_optimized = solve_optimized()
    print(f"Solution (optimized): {result_optimized}")
    
    # Verify both methods give the same result
    assert result == result_optimized, "Solutions don't match!"
    print(f"\nAnswer: {result}")
