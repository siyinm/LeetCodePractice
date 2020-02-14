class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size()==0) return 0;
        if (nums[0]>target) return 0;
        for (int i=0; i<nums.size();i++){
            if (nums[i]<target) continue;
            else if (nums[i]>=target) return i;
        }
        return nums.size();
    }
};
using namespace std;

class Solution2 {
public:
    int searchInsert(vector<int> &nums, int target) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }

        // 特判
        if (nums[size - 1] < target) {
            return size;
        }
        int left = 0;
        int right = size - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // 严格小于 target 的元素一定不是解
            if (nums[mid] < target) {
                // 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};

