#include <stdlib.h>

#include "list_node.h"

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* answer = malloc(sizeof(struct ListNode));
    if (answer == NULL) {
        return NULL;
    }
    answer->val = 0;
    answer->next = NULL;
    struct ListNode* cur = answer;
    int carry = 0;
    while (l1 != NULL || l2 != NULL || carry > 0) {
        int sum = carry;
        int carryOut = carry;
        if (l1 != NULL) {
            sum += l1->val;
            carryOut += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            carryOut += l2->val;
            l2 = l2->next;
        }
        sum %= 10;
        carry = carryOut / 10;
        cur->next = malloc(sizeof(struct ListNode));
        cur->next->val = sum;
        cur->next->next = NULL;
        cur = cur->next;
    }
    return answer->next;
}
