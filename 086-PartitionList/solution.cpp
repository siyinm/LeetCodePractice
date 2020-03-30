/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if (!head) return head;
        ListNode* left = new ListNode(0);
        ListNode* right = new ListNode(0);
        ListNode* rev1 = left;
        ListNode* rev2 = right;
        while (head){
            if (head->val < x){
                left->next = head;
                left = left->next;
                head = head->next;
            }
            else{
                right->next = head;
                right = right->next;
                head = head->next;
            }
        }
        
        left->next = rev2->next;
        right->next = NULL;
        return rev1->next;
    }
};
