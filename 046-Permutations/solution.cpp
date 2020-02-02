class Solution {
    vector<vector<int>> ans;
    vector<int> vec;
public:
    void helper(vector<int>& nums,int index){
        if (index == nums.size()){
            ans.push_back(vec);
            return;
        }
        for (int i=0; i<=index; i++){
            vec.insert(vec.begin()+i, nums[index]);
            helper(nums, index+1);
            vec.erase(vec.begin()+i );
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        if (nums.size()==0) return ans;
        helper(nums ,0);
        return ans;
        
    }
    
};
