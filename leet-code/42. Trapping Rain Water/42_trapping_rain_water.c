#define MAX_SIZE 20000
#define min(x, y) ((x) < (y) ? (x) : (y))

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

static void push(Stack* s, const int data) {
    s->top++;
    s->data[s->top] = data;
}

static int pop(Stack* s) {
    const int num = s->data[s->top];
    s->top--;
    return num;
}

static int is_empty(const Stack* s) {
    return s->top == -1;
}

int trap(int* height, int heightSize) {
    int sum = 0;
    Stack s = {.top = -1};
    for (int i = 0; i < heightSize; i++) {
        while (!is_empty(&s) && height[s.data[s.top]] < height[i]) {
            const int top = pop(&s);
            if (is_empty(&s)) {
                break;
            }
            const int high = min(height[s.data[s.top]], height[i]) - height[top];
            const int dist = i - s.data[s.top] - 1;
            sum += high * dist;
        }
        push(&s, i);
    }
    return sum;
}