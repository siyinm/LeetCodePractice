class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0;
        int right=int(height.size())-1;
        int maxcon=0;
        while(right>left){
            maxcon=max(maxcon,min(height[left],height[right])*(right-left));
            if (height[left]<height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return maxcon;
    }
};
