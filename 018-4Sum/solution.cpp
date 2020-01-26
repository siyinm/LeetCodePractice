class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> result;
        int size=nums.size();
        for(int a=0;a<size-3;++a)
        {
            if(a>0&&nums[a]==nums[a-1])continue;
            int min=nums[a]+nums[a+1]+nums[a+2]+nums[a+3];
            if (min>target) break;
            int max=nums[a]+nums[size-1]+nums[size-2]+nums[size-3];
            if (max<target) continue;
            
            for(int b=a+1;b<size-2;++b)//以下代码与三数之和一样的
            {
                if(b>a+1&&nums[b]==nums[b-1])continue;
                int i=b+1,j=size-1;
                int min=nums[a]+nums[b]+nums[i]+nums[i+1];
                int max=nums[a]+nums[b]+nums[j-1]+nums[j];
                if (min>target || max< target) continue;

                while(i<j)
                {
                    int sum=nums[a]+nums[b]+nums[i]+nums[j];
                    if(sum<target)
                        while(i<j&&nums[i]==nums[++i]);
                    else if(sum>target)
                        while(i<j&&nums[j]==nums[--j]);
                    else{
                        result.push_back(vector<int>{nums[a],nums[b],nums[i],nums[j]});
                        while(i<j&&nums[i]==nums[++i]);
                        while(i<j&&nums[j]==nums[--j]);
                    }
                }
            }
        }
        return result;
    }
};