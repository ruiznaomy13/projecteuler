#include <assert.h>
#include <stdio.h>

long sum_of_odd_squares(long n)
{
    assert(n > 0);
    long two_n = 2 * n;
    return (n * (two_n - 1) * (two_n + 1)) / 3;
}

int main(void)
{
    long limit;
    if (scanf("%ld", &limit) != 1) return 1;

    long n = limit / 2;
    printf("%ld\n", sum_of_odd_squares(n));

    return 0;
}
