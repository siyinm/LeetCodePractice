class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        if (len == 0 ) return -1;
        if (len ==1){
            if (nums[0] == target ) return 0;
            else return -1;
        }
        int left = 0;
        int right = len-1;
        while(left<right){
            int mid = left+(right-left)/2;
            if (nums[mid] == target) return mid;
            if (nums[left] <= nums[mid]){
                if (nums[left]<= target && target <= nums[mid]) {
                    right = mid;
                    continue;
                }
                else {
                    left = mid+1;
                    continue;
                }
            }
            else {
                if (nums[mid] <= target && target <= nums[right]){
                    left=mid;
                    continue;
                }
                else {
                    right = mid-1;
                }
            }
        }
        if (nums[left] == target) return left;
        if (nums[right] == target ) return right;
        return -1;
    }
};
