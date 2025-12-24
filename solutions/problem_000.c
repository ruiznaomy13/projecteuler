#include <assert.h>
#include <stdio.h>

/*
 * @precondition  n > 0
 * @postcondition Returns:
 *   1² + 3² + 5² + ... + (2n - 1)²
 *   = n(2n - 1)(2n + 1) / 3
 */
long sum_of_odd_squares(long n)
{
    assert(n > 0);

    long two_n = 2 * n;
    return (n * (two_n - 1) * (two_n + 1)) / 3;
}

int main(void)
{
    const long limit = 531000 / 2;

    long result = sum_of_odd_squares(limit);
    printf("%ld\n", result);

    return 0;
}
