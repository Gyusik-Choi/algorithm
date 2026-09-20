#include <stdlib.h>

static int get_min(const int a, const int b) {
    return a > b ? b : a;
}

int trap(int* height, int heightSize) {
    int* stack = malloc(sizeof(int) * heightSize);
    if (stack == NULL) {
        return 0;
    }
    int top = -1;
    int sum = 0;
    for (int i = 0; i < heightSize; i++) {
        while (top > -1 && height[stack[top]] < height[i]) {
            const int peek = stack[top--];
            if (top == -1) {
                break;
            }
            const int high = get_min(height[stack[top]], height[i]) - height[peek];
            const int dist = i - stack[top] - 1;
            sum += high * dist;
        }
        stack[++top] = i;
    }
    free(stack);
    return sum;
}