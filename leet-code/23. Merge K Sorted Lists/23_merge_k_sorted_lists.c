#include <stdbool.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct MinHeap {
    struct ListNode** arr;
    int size;
    int capacity;
};

static struct MinHeap create_min_heap(const int capacity) {
    struct MinHeap min_heap;
    min_heap.arr = malloc(sizeof(struct ListNode*) * (capacity + 1));
    min_heap.size = 0;
    min_heap.capacity = capacity;
    min_heap.arr[0] = NULL;
    return min_heap;
}

static void heap_push(struct MinHeap* heap, struct ListNode* node) {
    heap->arr[++heap->size] = node;
    int idx = heap->size;
    while (idx > 1 && heap->arr[idx / 2]->val > heap->arr[idx]->val) {
        struct ListNode* tmp = heap->arr[idx];
        heap->arr[idx] = heap->arr[idx / 2];
        heap->arr[idx / 2] = tmp;
        idx = idx / 2;
    }
}

static void heapify(struct MinHeap* heap, const int index) {
    int parent = index;
    const int left_child = parent * 2;
    const int right_child = parent * 2 + 1;
    if (left_child <= heap->size && heap->arr[parent]->val > heap->arr[left_child]->val) {
        parent = left_child;
    }
    if (right_child <= heap->size && heap->arr[parent]->val > heap->arr[right_child]->val) {
        parent = right_child;
    }
    if (index != parent) {
        struct ListNode* tmp = heap->arr[index];
        heap->arr[index] = heap->arr[parent];
        heap->arr[parent] = tmp;
        heapify(heap, parent);
    }
}

static struct ListNode* heap_pop(struct MinHeap* heap) {
    struct ListNode* top = heap->arr[1];
    heap->arr[1] = heap->arr[heap->size--];
    heapify(heap, 1);
    return top;
}

static bool heap_empty(const struct MinHeap* heap) {
    return heap->size == 0;
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    struct MinHeap min_heap = create_min_heap(listsSize);
    struct ListNode* root = malloc(sizeof(struct ListNode));
    root->val = 0;
    root->next = NULL;
    for (int i = 0; i < listsSize; i++) {
        if (lists[i] == NULL) {
            continue;
        }
        heap_push(&min_heap, lists[i]);
    }
    struct ListNode* cur = root;
    while (!heap_empty(&min_heap)) {
        struct ListNode* top = heap_pop(&min_heap);
        struct ListNode* next = top->next;
        top->next = NULL;
        cur->next = top;
        cur = cur->next;
        if (next != NULL) {
            heap_push(&min_heap, next);
        }
    }
    struct ListNode* answer = root->next;
    free(root);
    free(min_heap.arr);
    return answer;
}