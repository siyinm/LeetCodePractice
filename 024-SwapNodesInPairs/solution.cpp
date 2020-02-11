tion for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* fi = head;
        ListNode* se = head->next;
        ListNode* temp = NULL;
        fi -> next = se -> next;
        se -> next = fi;
        head = se;
        while( fi->next!= NULL ){
            temp = fi;
            fi = fi->next;
            if (fi->next == NULL) break;
            se = fi->next;
            temp->next=se;
            fi->next = se->next;
            se->next = fi;
        }
        return head;
    }
};
