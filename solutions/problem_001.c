#include <assert.h>
#include <stdio.h>

int sum_of_n(int n)
{
    assert(n > 0);
    return n * (n + 1) / 2;
}

int main(void)
{
    const int max = 1000;

    int limit = max - 1;
    int sum3 = 3 * sum_of_n(limit / 3);
    int sum5 = 5 * sum_of_n(limit / 5);
    int sum15 = 15 * sum_of_n(limit / 15);

    printf("%d\n", sum3 + sum5 - sum15);
    return 0;
}
