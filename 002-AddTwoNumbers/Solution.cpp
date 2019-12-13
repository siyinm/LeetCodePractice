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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p=l1;
        ListNode* q=l2;   
        ListNode* dummyHead=new ListNode(0);
        int carry=0;
        ListNode* curr=dummyHead;
        while(p!=NULL ||q!=NULL){
            int x=(p!=NULL)? p->val :0;
            int y=(q!=NULL)? q->val :0;
            int sum= carry + x + y;
            carry=sum / 10;
            curr->next=new ListNode(sum % 10);
            curr=curr->next;
            if (p!=NULL) p=p->next;
            if (q!=NULL) q=q->next;
        }
        if (carry) {
            curr->next=new ListNode(1);
        }
        return  dummyHead->next;
    }
    
};
