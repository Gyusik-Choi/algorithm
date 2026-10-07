#include <stddef.h>
#include "list_node.h"

static struct ListNode* reverse(struct ListNode* cur, struct ListNode* prev) {
    if (cur == NULL) {
        return prev;
    }
    struct ListNode* next = cur->next;
    cur->next = prev;
    return reverse(next, cur);
}

struct ListNode* reverseList(struct ListNode* head) {
    return reverse(head, NULL);
}