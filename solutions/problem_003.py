"""
Project Euler - Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def solve(n=600851475143):
    """
    Find the largest prime factor of the given number.
    
    Args:
        n: The number to find the largest prime factor of
        
    Returns:
        The largest prime factor of n
    """
    largest = 1
    
    # Divide by 2 until n is odd
    while n % 2 == 0:
        largest = 2
        n //= 2
    
    # Check odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        largest = n
    
    return largest


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_prime_factors(n):
    """Get all prime factors of a number."""
    factors = []
    
    # Divide by 2 until n is odd
    while n % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        n //= 2
    
    # Check odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            if factor not in factors:
                factors.append(factor)
            n //= factor
        factor += 2
    
    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == "__main__":
    result = solve()
    print(f"Largest prime factor: {result}")
    
    # Verify with example
    example_result = solve(13195)
    print(f"\nExample (13195): {example_result}")
    print(f"Prime factors of 13195: {get_prime_factors(13195)}")
    
    print(f"\nAnswer: {result}")
