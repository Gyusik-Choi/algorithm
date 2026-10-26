#include <stdbool.h>
#include <stdlib.h>

typedef struct Node {
    struct Node* prev;
    struct Node* next;
    int value;
} Node;

typedef struct {
    Node* head;
    Node* tail;
    int limit;
    int size;
} MyCircularDeque;


MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque* deq = malloc(sizeof(MyCircularDeque));
    deq->head = malloc(sizeof(Node));
    deq->head->value = -1;
    deq->tail = malloc(sizeof(Node));
    deq->tail->value = -1;
    deq->head->prev = NULL;
    deq->head->next = deq->tail;
    deq->tail->prev = deq->head;
    deq->tail->next = NULL;
    deq->limit = k;
    deq->size = 0;
    return deq;
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    return obj->size == 0;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    return obj->size == obj->limit;
}

bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if (myCircularDequeIsFull(obj)) {
        return false;
    }
    Node* oldNode = obj->head->next;
    Node* newNode = malloc(sizeof(Node));
    newNode->value = value;
    newNode->next = oldNode;
    newNode->prev = obj->head;
    obj->head->next = newNode;
    oldNode->prev = newNode;
    obj->size++;
    return true;
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if (myCircularDequeIsFull(obj)) {
        return false;
    }
    Node* oldNode = obj->tail->prev;
    Node* newNode = malloc(sizeof(Node));
    newNode->value = value;
    newNode->prev = oldNode;
    newNode->next = obj->tail;
    obj->tail->prev = newNode;
    oldNode->next = newNode;
    obj->size++;
    return true;
}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if (myCircularDequeIsEmpty(obj)) {
        return false;
    }
    Node* oldNext = obj->head->next;
    Node* newNext = oldNext->next;
    free(oldNext);
    obj->head->next = newNext;
    newNext->prev = obj->head;
    obj->size--;
    return true;
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if (myCircularDequeIsEmpty(obj)) {
        return false;
    }
    Node* oldPrev = obj->tail->prev;
    Node* newPrev = oldPrev->prev;
    free(oldPrev);
    obj->tail->prev = newPrev;
    newPrev->next = obj->tail;
    obj->size--;
    return true;
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if (myCircularDequeIsEmpty(obj)) {
        return -1;
    }
    return obj->head->next->value;
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if (myCircularDequeIsEmpty(obj)) {
        return -1;
    }
    return obj->tail->prev->value;
}

void myCircularDequeFree(MyCircularDeque* obj) {
    Node* cur = obj->head;
    while (cur != NULL) {
        Node* next = cur->next;
        free(cur);
        cur = next;
    }
    free(obj);
}

/**
 * Your MyCircularDeque struct will be instantiated and called as such:
 * MyCircularDeque* obj = myCircularDequeCreate(k);
 * bool param_1 = myCircularDequeInsertFront(obj, value);

 * bool param_2 = myCircularDequeInsertLast(obj, value);

 * bool param_3 = myCircularDequeDeleteFront(obj);

 * bool param_4 = myCircularDequeDeleteLast(obj);

 * int param_5 = myCircularDequeGetFront(obj);

 * int param_6 = myCircularDequeGetRear(obj);

 * bool param_7 = myCircularDequeIsEmpty(obj);

 * bool param_8 = myCircularDequeIsFull(obj);

 * myCircularDequeFree(obj);
*/