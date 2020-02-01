class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l=0;
        int r=1;
        int size=nums.size();
        if (size<=1) return size;
        else 
        while (r<size){
            if (nums[r]==nums[r-1] ){
                r++;
                continue;
            }
            else{
                l++;
                nums[l]= nums[r];
                r++;
            }
        }
        
        return l+1;
    }
};
