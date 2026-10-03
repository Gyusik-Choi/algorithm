#include <stdbool.h>
#include <stddef.h>
#include "234_palindrome_linked_list.h"

/**
* Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode* left = NULL;
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        struct ListNode* next = slow->next;
        slow->next = left;
        left = slow;
        slow = next;
    }

    struct ListNode* right = slow;
    // head 요소의 갯수가 홀수면 한칸 더 앞으로 이동
    if (fast != NULL) {
        right = right->next;
    }

    while (left != NULL && right != NULL) {
        if (left->val != right->val) {
            return false;
        }
        left = left->next;
        right = right->next;
    }
    return true;
}