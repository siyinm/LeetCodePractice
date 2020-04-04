//stack
class Solution_stack {
public:
    int trap(vector<int>& height) {
        stack<int> st;
        int curr=0;
        int ans=0;
        while (curr< height.size()){
            while (!st.empty() && height[st.top()] < height[curr]){
                int top=st.top();
                st.pop();
                if (st.empty()) 
                    break;
                int bh=min(height[curr], height[st.top()]) - height[top];
                ans+=(curr-st.top()-1) * bh;           
            }
            st.push(curr++);
        }
        return ans;
    
    }
};

//two_pointers
class Solution_twoPointers {
public:
    int trap(vector<int>& height) {
        int left=height.size()-2;
        int right=height.size()-1;
        int ans=0;
        while (right>0){
            //find the left max, or just larger than right
            for (int i=left; i>=0; --i){
                if (height[left]>height[right]) break;
                if (height[i]>height[left]) left=i;
            }

            //calculate the rain between left and right: (right-left)*min(left,right)-middle
            int middle=0;
            for (int j=left+1; j<right; j++) middle+=height[j];
            ans+= (right-left-1)*min(height[left], height[right]) -middle;
            //std::cout<<ans<<std::endl;
            right=left;
            left--;
        
        }
        return ans;
    }
};
//two pointers


