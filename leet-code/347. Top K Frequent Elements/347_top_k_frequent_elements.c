#include <stdbool.h>
#include <stdlib.h>

static const int NO_EXIST = -10001;
static const int DEFAULT_CAPACITY = 16;

struct Item {
    int key;
    int value;
};

struct Heap {
    struct Item** arr;
    int size;
};

struct Node {
    int key;
    int value;
    struct Node* next;
};

struct HashMap {
    struct Node** arr;
    int capacity;
    int threshold;
    int size;
};

static struct Item* create_item(const int key, const int value) {
    struct Item* item = malloc(sizeof(struct Item));
    item->key = key;
    item->value = value;
    return item;
}

static struct Heap* create_heap(const int capacity) {
    struct Heap* heap = malloc(sizeof(struct Heap));
    heap->arr = malloc(sizeof(struct Item*) * (capacity + 1));
    heap->arr[0] = create_item(NO_EXIST, NO_EXIST);
    heap->size = 0;
    return heap;
}

static void free_heap(struct Heap* heap) {
    for (int i = 0; i <= heap->size; i++) {
        free(heap->arr[i]);
    }
    free(heap->arr);
    free(heap);
}

static struct Node* create_node(const int key, const int value) {
    struct Node* node = malloc(sizeof(struct Node));
    node->key = key;
    node->value = value;
    node->next = NULL;
    return node;
}

static void heap_push(struct Heap* heap, struct Item* item) {
    heap->arr[++heap->size] = item;
    int idx = heap->size;
    while (idx > 1 && heap->arr[idx / 2]->value < heap->arr[idx]->value) {
        struct Item* tmp = heap->arr[idx];
        heap->arr[idx] = heap->arr[idx / 2];
        heap->arr[idx / 2] = tmp;
        idx = idx / 2;
    }
}

static void heapify(struct Heap* heap, const int index) {
    int parent = index;
    const int left_child = index * 2;
    const int right_child = index * 2 + 1;
    if (left_child <= heap->size && heap->arr[left_child]->value > heap->arr[parent]->value) {
        parent = left_child;
    }
    if (right_child <= heap->size && heap->arr[right_child]->value > heap->arr[parent]->value) {
        parent = right_child;
    }
    if (index != parent) {
        struct Item* temp = heap->arr[index];
        heap->arr[index] = heap->arr[parent];
        heap->arr[parent] = temp;
        heapify(heap, parent);
    }
}

static struct Item* heap_pop(struct Heap* heap) {
    if (heap->size == 0) {
        return NULL;
    }
    struct Item* item = heap->arr[1];
    heap->arr[1] = heap->arr[heap->size--];
    heapify(heap, 1);
    return item;
}

static struct HashMap* create_hash_map(void) {
    struct HashMap* hash_map = malloc(sizeof(struct HashMap));
    hash_map->arr = calloc(DEFAULT_CAPACITY, sizeof(struct Node*));
    hash_map->capacity = DEFAULT_CAPACITY;
    hash_map->threshold = DEFAULT_CAPACITY * 3 / 4;
    hash_map->size = 0;
    return hash_map;
}

static void free_hash_map(struct HashMap* hash_map) {
    for (int i = 0; i < hash_map->capacity; i++) {
        struct Node* node = hash_map->arr[i];
        while (node != NULL) {
            struct Node* next = node->next;
            free(node);
            node = next;
        }
    }
    free(hash_map->arr);
    free(hash_map);
}

static int get_hash_code(const int key) {
    return key;
}

static int mix_bits(const int hash) {
    return hash ^ (hash >> 16);
}

static int get_hash_index(const int capacity, const int key) {
    const int mixed_hash_key = mix_bits(get_hash_code(key));
    return mixed_hash_key & (capacity - 1);
}

static int get_hash_value(const struct HashMap* hash_map, const int key) {
    const int index = get_hash_index(hash_map->capacity, key);
    const struct Node* cur = hash_map->arr[index];
    while (cur != NULL) {
        if (cur->key == key) {
            return cur->value;
        }
        cur = cur->next;
    }
    return NO_EXIST;
}

static bool should_increase(const struct HashMap* hash_map) {
    return hash_map->size >= hash_map->threshold;
}

static void increase_capacity_and_threshold(struct HashMap* hash_map) {
    hash_map->capacity = hash_map->capacity << 1;
    hash_map->threshold = hash_map->threshold << 1;
}

static bool put(struct Node** arr, const int capacity, const int key, const int value) {
    const int index = get_hash_index(capacity, key);
    if (arr[index] == NULL) {
        arr[index] = create_node(key, value);
        return true;
    }
    struct Node* prev = NULL;
    struct Node* cur = arr[index];
    while (cur != NULL) {
        if (cur->key == key) {
            cur->value = value;
            return false;
        }
        prev = cur;
        cur = cur->next;
    }
    prev->next = create_node(key, value);
    return true;
}


static void re_allocate(struct HashMap* hash_map) {
    const int capacity = hash_map->capacity;
    const int old_capacity = capacity >> 1;
    struct Node** new_arr = calloc(capacity, sizeof(struct Node*));
    for (int i = 0; i < old_capacity; i++) {
        struct Node* node = hash_map->arr[i];
        while (node != NULL) {
            struct Node* next = node->next;
            put(new_arr, hash_map->capacity, node->key, node->value);
            free(node);
            node = next;
        }
    }
    free(hash_map->arr);
    hash_map->arr = new_arr;
}

static void put_hash_map(struct HashMap* hash_map, const int key, const int value) {
    if (put(hash_map->arr, hash_map->capacity, key, value)) {
        hash_map->size++;
        if (should_increase(hash_map)) {
            increase_capacity_and_threshold(hash_map);
            re_allocate(hash_map);
        }
    }
}

/**
* Note: The returned array must be malloced, assume caller calls free().
 */
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    struct HashMap* map = create_hash_map();
    for (int i = 0; i < numsSize; i++) {
        const int value = get_hash_value(map, nums[i]);
        if (value == NO_EXIST) {
            put_hash_map(map, nums[i], 1);
        } else {
            put_hash_map(map, nums[i], value + 1);
        }
    }
    struct Heap* heap = create_heap(numsSize);
    for (int i = 0; i < map->capacity; i++) {
        const struct Node* node = map->arr[i];
        while (node != NULL) {
            heap_push(heap, create_item(node->key, node->value));
            node = node->next;
        }
    }
    *returnSize = k;
    int* answer = malloc(sizeof(int) * k);
    for (int i = 0; i < k; i++) {
        struct Item* item = heap_pop(heap);
        answer[i] = item->key;
        free(item);
    }
    free_hash_map(map);
    free_heap(heap);
    return answer;
}