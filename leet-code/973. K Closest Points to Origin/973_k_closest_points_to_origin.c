#include <stdlib.h>

struct Point {
    int* point;
    int distance;
};

struct Heap {
    struct Point** points;
    int size;
    int capacity;
};

static struct Heap create_heap(const int size) {
    struct Heap heap;
    heap.points = malloc(sizeof(struct Point*) * (size + 1));
    heap.size = 0;
    heap.capacity = size;
    heap.points[0] = NULL;
    return heap;
}

static void heap_push(struct Heap* heap, struct Point* point) {
    heap->points[++heap->size] = point;
    int idx = heap->size;
    while (idx > 1 && heap->points[idx / 2]->distance > heap->points[idx]->distance) {
        struct Point* tmp = heap->points[idx / 2];
        heap->points[idx / 2] = heap->points[idx];
        heap->points[idx] = tmp;
        idx = idx / 2;
    }
}

static void heapify(struct Heap* heap, const int idx) {
    int parent = idx;
    const int left_child = idx * 2;
    const int right_child = left_child + 1;
    if (left_child <= heap->size && heap->points[parent]->distance > heap->points[left_child]->distance) {
        parent = left_child;
    }
    if (right_child <= heap->size && heap->points[parent]->distance > heap->points[right_child]->distance) {
        parent = right_child;
    }
    if (idx != parent) {
        struct Point* tmp = heap->points[idx];
        heap->points[idx] = heap->points[parent];
        heap->points[parent] = tmp;
        heapify(heap, parent);
    }
}

static struct Point* heap_pop(struct Heap* heap) {
    struct Point* tmp = heap->points[1];
    heap->points[1] = heap->points[heap->size];
    heap->size--;
    heapify(heap, 1);
    return tmp;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int** returnColumnSizes) {
    struct Heap heap = create_heap(pointsSize);
    for (int i = 0; i < pointsSize; i++) {
        struct Point* p = malloc(sizeof(struct Point));
        p->point = points[i];
        p->distance = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1]);
        heap_push(&heap, p);
    }

    int** answer = malloc(sizeof(int*) * k);
    *returnColumnSizes = malloc(sizeof(int) * k);
    for (int i = 0; i < k; i++) {
        struct Point* p = heap_pop(&heap);
        answer[i] = malloc(sizeof(int) * 2);
        answer[i][0] = p->point[0];
        answer[i][1] = p->point[1];
        free(p);
        (*returnColumnSizes)[i] = 2;
    }
    for (int i = 1; i <= heap.size; i++) {
        free(heap.points[i]);
    }
    free(heap.points);
    *returnSize = k;
    return answer;
}