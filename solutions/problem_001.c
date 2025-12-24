#include <assert.h>
#include <stdio.h>

/*
 * @precondition  n > 0
 * @postcondition Returns:
 *   1 + 2 + 3 + ... + n = n(n + 1) / 2
 */
int sum_of_n(int n)
{
    assert(n > 0);
    return n * (n + 1) / 2;
}

int main(void)
{
    const int max = 999;

    int sum_3 = 3 * sum_of_n(max / 3);
    int sum_5 = 5 * sum_of_n(max / 5);
    int sum_15 = 15 * sum_of_n(max / 15);

    int result = sum_3 + sum_5 - sum_15;
    printf("%d\n", result);

    return 0;
}
