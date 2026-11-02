#include <stdlib.h>
#include <stdbool.h>

static const int DEFAULT_CAPACITY = 16;
static const float DEFAULT_LOAD_FACTOR = 0.75f;

typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

typedef struct {
    int capacity;
    int threshold;
    int size;
    Node** table;
} MyHashMap;

static Node* create_node(const int key, const int value) {
    Node* new_node = malloc(sizeof(Node));
    new_node->key = key;
    new_node->value = value;
    new_node->next = NULL;
    return new_node;
}

static MyHashMap* myHashMapCreate() {
    MyHashMap* map = malloc(sizeof(MyHashMap));
    map->capacity = DEFAULT_CAPACITY;
    map->threshold = DEFAULT_CAPACITY * DEFAULT_LOAD_FACTOR;
    map->size = 0;
    map->table = calloc(map->capacity, sizeof(Node*));
    return map;
}

static int get_hash_code(const int key) {
    return key;
}

static int mix_bits(const int hash) {
    return hash ^ (hash >> 16);
}

static int get_index(const int key, const int capacity) {
    const int mixed_hash = mix_bits(get_hash_code(key));
    return mixed_hash & (capacity - 1);
}

static bool put(Node** table, const int key, const int value, const int capacity) {
    const int index = get_index(key, capacity);
    if (table[index] == NULL) {
        Node* new_node = create_node(key, value);
        table[index] = new_node;
        return true;
    }
    Node* prev = NULL;
    Node* node = table[index];
    while (node != NULL) {
        if (node->key == key) {
            node->value = value;
            return false;
        }
        prev = node;
        node = node->next;
    }
    Node* new_node = create_node(key, value);
    prev->next = new_node;
    return true;
}

static void re_allocate(MyHashMap* map, int capacity) {
    Node** new_table = calloc(map->capacity, sizeof(Node*));
    for (int i = 0; i < capacity; i++) {
        Node* node = map->table[i];
        while (node != NULL) {
            Node* next = node->next;
            put(new_table, node->key, node->value, map->capacity);
            free(node);
            node = next;
        }
    }
    free(map->table);
    map->table = new_table;
}

static void increase_hash_map(MyHashMap* map) {
    map->size++;
    if (map->size >= map->threshold) {
        const int old_capacity = map->capacity;
        map->capacity = map->capacity << 1;
        map->threshold = map->threshold << 1;
        re_allocate(map, old_capacity);
    }
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    if (put(obj->table, key, value, obj->capacity)) {
        increase_hash_map(obj);
    }
}

int myHashMapGet(MyHashMap* obj, int key) {
    const int index = get_index(key, obj->capacity);
    if (obj->table[index] == NULL) {
        return -1;
    }
    const Node* node = obj->table[index];
    while (node != NULL) {
        if (node->key == key) {
            return node->value;
        }
        node = node->next;
    }
    return -1;
}

void myHashMapRemove(MyHashMap* obj, int key) {
    const int index = get_index(key, obj->capacity);
    if (obj->table[index] == NULL) {
        return;
    }
    Node* node = obj->table[index];
    if (node->key == key) {
        obj->table[index] = obj->table[index]->next;
        free(node);
        obj->size--;
        return;
    }
    Node* prev = node;
    node = node->next;
    while (node != NULL) {
        if (node->key == key) {
            prev->next = node->next;
            free(node);
            obj->size--;
            return;
        }
        prev = node;
        node = node->next;
    }
}

void myHashMapFree(MyHashMap* obj) {
    for (int i = 0; i < obj->capacity; i++) {
        Node* node = obj->table[i];
        while (node != NULL) {
            Node* next = node->next;
            free(node);
            node = next;
        }
    }
    free(obj->table);
    free(obj);
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);

 * int param_2 = myHashMapGet(obj, key);

 * myHashMapRemove(obj, key);

 * myHashMapFree(obj);
*/