#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int compareLogs(const void* a, const void* b) {
    const char* logA = *(const char**)a;
    const char* logB = *(const char**)b;

    const char* wordA = strchr(logA, ' ') + 1;
    const char* wordB = strchr(logB, ' ') + 1;

    const int cmp = strcmp(wordA, wordB);
    if (cmp != 0) {
        return cmp;
    }
    return strcmp(logA, logB);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** reorderLogFiles(char** logs, int logsSize, int* returnSize) {
    int letter_size = 0, digit_size = 0;
    char** result = malloc(logsSize * sizeof(char*));
    char** letters = malloc(logsSize * sizeof(char*));
    char** digits = malloc(logsSize * sizeof(char*));
    for (int i = 0; i < logsSize; i++) {
        char* copied_log = strdup(logs[i]);
        strtok(copied_log, " ");
        const char* log_word = strtok(NULL, " ");
        if (isdigit(log_word[0])) {
            digits[digit_size] = logs[i];
            digit_size++;
        } else {
            letters[letter_size] = logs[i];
            letter_size++;
        }
        free(copied_log);
    }

    qsort(letters, letter_size, sizeof(char*), compareLogs);

    int idx = 0;
    for (int i = 0; i < letter_size; i++) {
        result[idx++] = letters[i];
    }
    for (int i = 0; i < digit_size; i++) {
        result[idx++] = digits[i];
    }
    *returnSize = idx;

    free(letters);
    free(digits);

    return result;
}
