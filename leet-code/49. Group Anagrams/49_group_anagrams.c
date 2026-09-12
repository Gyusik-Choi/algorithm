#include <stdlib.h>
#include <string.h>

static int cmp(const void* a, const void* b) {
    return *(char*)a - *(char*)b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    char*** result = malloc(sizeof(char**) * strsSize);
    char** keys = malloc(sizeof(char*) * strsSize);
    *returnColumnSizes = malloc(sizeof(int) * strsSize);
    *returnSize = 0;

    for (int i = 0; i < strsSize; i++) {
        const int len = strlen(strs[i]);
        char* key = malloc(len + 1);
        strcpy(key, strs[i]);
        qsort(key, len, sizeof(char), cmp);

        int key_idx = -1;
        for (int j = 0; j < *returnSize; j++) {
            if (strcmp(key, keys[j]) == 0) {
                key_idx = j;
                break;
            }
        }

        if (key_idx == -1) {
            key_idx = (*returnSize)++;
            keys[key_idx] = key;
            result[key_idx] = malloc(sizeof(char*) * strsSize);
            (*returnColumnSizes)[key_idx] = 0;
        } else {
            free(key);
        }

        result[key_idx][(*returnColumnSizes)[key_idx]++] = strs[i];
    }

    for (int i = 0; i < *returnSize; i++) {
        free(keys[i]);
    }
    free(keys);
    return result;
}
