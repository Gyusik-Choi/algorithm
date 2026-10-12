#include <stddef.h>
#include "list_node.h"

struct ListNode* oddEvenList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct ListNode* odd = head;
    struct ListNode* even = head->next;
    struct ListNode* evenRef = head->next;

    while (odd->next != NULL && odd->next->next != NULL) {
        odd->next = odd->next->next;
        even->next = odd->next->next;
        odd = odd->next;
        even = even->next;
    }

    odd->next = evenRef;
    return head;
}