#include <stdio.h>

int fib_recursion(int i) {
    if (i<=0) {
        return -1;
    }
    if (i==1) {
        return 1;
    }
    if (i==2) {
        return 1;
    }
    return fib_recursion(i-1)+fib_recursion(i-2);
}

int fib_iteration(int i) {
    int cur = 1;
    int prev = 1;
    int temp;
    int j;

    if (i<=0) {
        return -1;
    }
    if (i==1) {
        return 1;
    }

    for (j=2; j<i; j++) {
        temp = cur;
        cur = cur + prev;
        prev = temp;
    }
    return cur;
}

void draw_triangle(int i) {
    int j;
    int k;

    for (j=0; j<i; j++) {
        for (k=0; k<j; k++) {
            printf("*");
        } printf("\n");
    }
}



int main() {
    printf("Hello world!\n");
    printf("The 5th fibonacci number is: %d\n", fib_recursion(5));
    printf("The 7th fibonacci number is: %d\n", fib_iteration(7));
    printf("Here's a triangle:\n");
    draw_triangle(10);
    return 0;
}
