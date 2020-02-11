class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l=0;
        int r=0;
        int size=nums.size();
        //if (size<=1) return size;
        while(r<size){
            if (nums[r]==val){
                r++;
                continue;
            }
            else {
                nums[l]=nums[r];
                l++;
                r++;
            }
        }
        return l;
    }
    
};



