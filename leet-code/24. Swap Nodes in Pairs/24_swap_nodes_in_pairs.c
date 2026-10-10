#include <stdlib.h>

#include "list_node.h"

struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* root = malloc(sizeof(struct ListNode));
    if (root == NULL) {
        return head;
    }
    root->val = 0;
    root->next = head;
    struct ListNode* prev = root;
    struct ListNode* cur = head;

    while (cur != NULL && cur->next != NULL) {
        struct ListNode* next = cur->next;
        struct ListNode* nextNext = next->next;

        prev->next = next;
        next->next = cur;
        cur->next = nextNext;

        prev = cur;
        cur = nextNext;
    }

    struct ListNode* answer = root->next;
    free(root);
    return answer;
}