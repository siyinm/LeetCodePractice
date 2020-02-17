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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode* res = new ListNode(0);
        ListNode* head =res;
        while (l1 && l2){
            if (l1->val < l2-> val){
                res->next = l1;
                l1 = l1->next;
            } 
            else {
                res->next = l2;
                l2 = l2->next;
            }
            res = res->next;
        }
        if (l1) res->next = l1;
        if (l2) res->next = l2;
        return head->next;
        
    }
};


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        if (l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2) ;
            return l1;
        }
        else {
            l2->next = mergeTwoLists(l1, l2->next) ;
            return l2;
        }
        
    }
};
