class Solution1 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL) return l2;
        if (l2 == NULL) return l1;
        ListNode* pre = new ListNode(0);
        ListNode* cur = pre;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }

        cur->next = l1 != NULL ? l1 : l2;

        return pre->next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int len = lists.size();
        if (len == 0) return NULL;
        // 分组间隔每次扩大两倍
        int interval = 1;
        while (interval < len) {
            // 根据当前间隔，两两合并，合并后的结果保存在两个链表的第一个
            for (int i = 0; i < len - interval; i += 2 * interval) {
                lists[i]  = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }

        return lists[0];
    }
};

class Solution2 {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* ans= NULL;
        if (lists.empty()) return ans;
        for (int i=0;i<lists.size()-1;i++){
            lists[i+1]= mergeTwoLists(lists[i],lists[i+1]);
        }
        return lists[lists.size()-1];
    }
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


class Solution3 {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* ans= NULL;
        for (int i=0;i<lists.size();i++){
            if (!lists[i]) {
                lists.erase(lists.begin()+i);
                i--;
            }
        } 
        if (lists.empty()) return ans;
        ListNode* res =new ListNode(0);
        return help(lists, res,res)->next;
    }
    
    ListNode* help(vector<ListNode*>& lists, ListNode* res,ListNode* now) {
        if (lists.empty()) return res;
        int min=0;
        for (int i=0;i<lists.size();i++){
            if (lists[i]->val < lists[min]->val) min=i;
        }
        now->next=lists[min];
        now=now->next;
        if (lists[min]->next) lists[min]=lists[min]->next;
        else lists.erase(lists.begin()+min);
        return help(lists, res, now);
    }


};