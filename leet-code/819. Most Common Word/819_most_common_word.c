#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmp(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

static bool is_banned(const char* word, char** banned, const int banned_size) {
    for (int i = 0; i < banned_size; i++) {
        if (strcmp(word, banned[i]) == 0) {
            return true;
        }
    }
    return false;
}

char* mostCommonWord(char* paragraph, char** banned, int bannedSize) {
    int n = 0;
    char* words[1000];
    char* p = paragraph;
    while (*p) {
        if (!isalpha((unsigned char)*p)) {
            p++;
            continue;
        }

        char* start = p;
        while (isalpha((unsigned char)*p)) {
            *p = (char)tolower((unsigned char)*p);
            p++;
        }
        if (*p) {
            *p = '\0';
            p++;
        }
        if (!is_banned(start, banned, bannedSize)) {
            words[n++] = start;
        }
    }

    qsort(words, n, sizeof(char*), cmp);

    char* most_common_word = NULL;
    int max_count = 0;
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && strcmp(words[i], words[j]) == 0) {
            j++;
        }
        if (j - i > max_count) {
            max_count = j - i;
            most_common_word = words[i];
        }
        i = j;
    }
    return most_common_word;
}
