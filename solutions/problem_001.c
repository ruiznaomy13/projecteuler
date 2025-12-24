#include <assert.h>
#include <stdio.h>

/*
 * @precondition  n > 0
 * @postcondition Returns 1 + 2 + 3 + ... + n = n(n + 1) / 2
 */
int sum_of_n(int n)
{
    assert(n > 0);

    return (n * (n + 1)) / 2;
}

int main(void)
{
    const int LIMIT = 1000 - 1;
    const int sum_mul_of_three = 3 * sum_of_n(LIMIT / 3);
    const int sum_mul_of_five = 5 * sum_of_n(LIMIT / 5);
    const int sum_mul_of_fifteen = 15 * sum_of_n(LIMIT / 15);
    int       result = sum_mul_of_three + sum_mul_of_five - sum_mul_of_fifteen;
    printf("%d\n", result);

    return 0;
}
