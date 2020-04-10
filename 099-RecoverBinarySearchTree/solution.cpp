/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> res;
    TreeNode* pre = new TreeNode(INT_MIN);
    TreeNode* t1;
    TreeNode* t2;
    void inorderTraversal(TreeNode* root) {
        if (root == nullptr) return ;
        else{
            inorderTraversal(root->left);
            if (pre != nullptr && pre->val > root->val){
                if (t1 == nullptr) t1 = pre;
                t2 = root;
            }
            pre = root;   
            inorderTraversal(root->right);    
        }
    }
    void recoverTree(TreeNode* root) {
        if (root == nullptr) return;
        t1 = nullptr;
        t2 = nullptr;
        inorderTraversal(root);
        if (t1 != nullptr){
            int temp = t1->val;
            t1->val = t2->val;
            t2->val = temp;
        }
        
    }
};
