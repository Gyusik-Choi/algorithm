#include <stdbool.h>
#include <stdlib.h>

#define CAP 101

/**
 * 큐에 최대 100개가 들어올 수 있는데
 * 크기를 101 로 지정해서 한 칸을 비워둔다
 * 이렇게 해야 front, rear 가 같을 때
 * 비었는지 꽉 찼는지 구분할 수 없는 상태에 빠지지 않는다
 * 예를 들어, 크기가 4일때 한 칸을 비워두지 않은채로
 * 4번 큐에 원소를 추가하면 rear 가 3까지 올라갔다가 다시 0으로 돌아온다
 * 그러면 최초에는 front 와 rear 가 같으면 큐가 빈 상태지만
 * 이때는 front 와 rear 가 같을때 큐가 꽉 찬 상태를 가리킨다
 */
typedef struct {
    int data[CAP];
    int front;
    int rear;
} Queue;

Queue* queueCreate() {
    return calloc(1, sizeof(Queue));
}

void q_push(Queue* q, int x) {
    q->data[q->rear % CAP] = x;
    q->rear = (q->rear + 1) % CAP;
}

int q_pop(Queue* q) {
    const int pop = q->data[q->front];
    q->front = (q->front + 1) % CAP;
    return pop;
}

int q_top(Queue* q) {
    return q->data[q->front];
}

bool q_empty(Queue* q) {
    return q->front == q->rear;
}

typedef struct {
    Queue* q1;
    Queue* q2;
} MyStack;

MyStack* myStackCreate() {
    MyStack* obj = malloc(sizeof(MyStack));
    obj->q1 = queueCreate();
    obj->q2 = queueCreate();
    return obj;
}

void myStackPush(MyStack* obj, int x) {
    while (!q_empty(obj->q1)) {
        q_push(obj->q2, q_pop(obj->q1));
    }
    q_push(obj->q1, x);
    while (!q_empty(obj->q2)) {
        q_push(obj->q1, q_pop(obj->q2));
    }
}

int myStackPop(MyStack* obj) {
    return q_pop(obj->q1);
}

int myStackTop(MyStack* obj) {
    return q_top(obj->q1);
}

bool myStackEmpty(MyStack* obj) {
    return q_empty(obj->q1);
}

void myStackFree(MyStack* obj) {
    free(obj->q1);
    free(obj->q2);
    free(obj);
}

// typedef struct {
//     int q1[CAP];
//     int t1;
//     int q2[CAP];
//     int t2;
// } MyStack;
//
// MyStack* myStackCreate() {
//     return calloc(1, sizeof(MyStack));
// }
//
// void myStackPush(MyStack* obj, int x) {
//     obj->t2 = 0;
//     for (int i = 0; i < obj->t1; i++) {
//         obj->q2[obj->t2++] = obj->q1[i];
//     }
//     obj->t1 = 0;
//     obj->q1[obj->t1++] = x;
//     for (int i = 0; i < obj->t2; i++) {
//         obj->q1[obj->t1++] = obj->q2[i];
//     }
// }
//
// int myStackPop(MyStack* obj) {
//     const int pop = obj->q1[0];
//     for (int i = 1; i < obj->t1; i++) {
//         obj->q1[i - 1] = obj->q1[i];
//     }
//     obj->t1--;
//     return pop;
// }
//
// int myStackTop(MyStack* obj) {
//     return obj->q1[0];
// }
//
// bool myStackEmpty(MyStack* obj) {
//     return obj->t1 == 0;
// }
//
// void myStackFree(MyStack* obj) {
//     free(obj);
// }

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);

 * int param_2 = myStackPop(obj);

 * int param_3 = myStackTop(obj);

 * bool param_4 = myStackEmpty(obj);

 * myStackFree(obj);
*/