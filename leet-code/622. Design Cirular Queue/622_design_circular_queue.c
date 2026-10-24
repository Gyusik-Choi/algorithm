#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* arr;
    int length;
    int front;
    int rear;
} MyCircularQueue;


MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue* q = malloc(sizeof(MyCircularQueue));
    q->length = k + 1;
    q->arr = malloc(sizeof(int) * q->length);
    for (int i = 0; i < q->length; i++) {
        q->arr[i] = -1;
    }
    q->front = 0;
    q->rear = 0;
    return q;
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->front == obj->rear;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->front == (obj->rear + 1) % obj->length;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (myCircularQueueIsFull(obj)) {
        return false;
    }
    obj->arr[obj->rear] = value;
    obj->rear = (obj->rear + 1) % obj->length;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj)) {
        return false;
    }
    obj->arr[obj->front] = -1;
    obj->front = (obj->front + 1) % obj->length;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj)) {
        return -1;
    }
    return obj->arr[obj->front];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj)) {
        return -1;
    }
    return obj->arr[(obj->rear - 1 + obj->length) % obj->length];
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->arr);
    free(obj);
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);

 * bool param_2 = myCircularQueueDeQueue(obj);

 * int param_3 = myCircularQueueFront(obj);

 * int param_4 = myCircularQueueRear(obj);

 * bool param_5 = myCircularQueueIsEmpty(obj);

 * bool param_6 = myCircularQueueIsFull(obj);

 * myCircularQueueFree(obj);
*/