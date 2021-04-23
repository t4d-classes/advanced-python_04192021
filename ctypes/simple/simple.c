#include <stdio.h>
#include "simple.h"

void print_me()
{
    printf("Python and C are super cool together!\n");
}

void print_msg(char *msg)
{
    printf("%s\n", msg);
}

float add_two_nums(float x, float y)
{
    return x + y;
}

int sum_nums(int *data, int len)
{
    int sum;

    for(int i = 0; i < len; ++i) {
        sum += data[i];
    }

    return sum;
}