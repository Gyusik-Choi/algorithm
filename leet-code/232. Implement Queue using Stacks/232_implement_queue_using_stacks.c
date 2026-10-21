#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* arr;
    int top;
    int max_size;
} Stack;

Stack* create_stack() {
    Stack* s = malloc(sizeof(Stack));
    s->arr = malloc(sizeof(int) * 100);
    s->top = 0;
    s->max_size = 100;
    return s;
}

void s_push(Stack* obj, int x) {
    obj->arr[obj->top++] = x;
}

int s_pop(Stack* obj) {
    const int pop = obj->arr[obj->top - 1];
    obj->top--;
    return pop;
}

int s_top(Stack* obj) {
    return obj->arr[obj->top - 1];
}

bool s_full(Stack* obj) {
    if (obj->top == obj->max_size) {
        return true;
    }
    return false;
}

bool s_empty(Stack* obj) {
    if (obj->top == 0) {
        return true;
    }
    return false;
}

void s_free(Stack* obj) {
    free(obj->arr);
    free(obj);
}

typedef struct {
    Stack* q1;
    Stack* q2;
} MyQueue;


MyQueue* myQueueCreate() {
    MyQueue* q = malloc(sizeof(MyQueue));
    q->q1 = create_stack();
    q->q2 = create_stack();
    return q;
}

void myQueuePush(MyQueue* obj, int x) {
    while (s_empty(obj->q1) == false) {
        s_push(obj->q2, s_pop(obj->q1));
    }
    s_push(obj->q1, x);
    while (s_empty(obj->q2) == false) {
        s_push(obj->q1, s_pop(obj->q2));
    }
}

int myQueuePop(MyQueue* obj) {
    return s_pop(obj->q1);
}

int myQueuePeek(MyQueue* obj) {
    return s_top(obj->q1);
}

bool myQueueEmpty(MyQueue* obj) {
    return s_empty(obj->q1);
}

void myQueueFree(MyQueue* obj) {
    s_free(obj->q1);
    s_free(obj->q2);
    free(obj);
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);

 * int param_2 = myQueuePop(obj);

 * int param_3 = myQueuePeek(obj);

 * bool param_4 = myQueueEmpty(obj);

 * myQueueFree(obj);
*/