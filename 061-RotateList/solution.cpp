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
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode* p = head;
        if (!p || !p->next) return head;
        int n = 1;
        while(p->next){
            p = p->next;
            n++;
        }
        p->next = head;
        p = p->next;
        k=k%n;
        for (int i = 0; i < n-k-1; i++) {
            p = p->next;
        }
        ListNode* res = p->next;
        p->next = NULL;
        return res;
    }
};