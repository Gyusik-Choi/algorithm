#include <stddef.h>
#include <stdlib.h>

#include "list_node.h"

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (left == right) {
        return head;
    }

    struct ListNode* root = malloc(sizeof(struct ListNode));
    root->next = head;
    struct ListNode* curPrev = root;
    struct ListNode* cur = head;
    for (int i = 1; i < left; i++) {
        curPrev = cur;
        cur = cur->next;
    }

    struct ListNode* curStart = cur;
    struct ListNode* prev = NULL;
    struct ListNode* next = NULL;
    for (int i = left; i <= right; i++) {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }

    curPrev->next = prev;
    curStart->next = next;
    struct ListNode* answer = root->next;
    free(root);
    return answer;
}