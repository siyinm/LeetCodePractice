class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for (int i=0; i < nums.size(); ++i){
            for (int j=i+1; j < nums.size() ; ++j){
                if (nums[i]+nums[j]==target){
                    result.push_back(i);
                    result.push_back(j);
                }
            }
        }
        return result;
    }
};


//执行用时 : 524 ms, 在所有 cpp 提交中击败了 6.55% 的用户
//内存消耗 : 9.3 MB, 在所有 cpp 提交中击败了 79.36% 的用户

class Solution2 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> a;//提供一对一的hash
        vector<int> b(2,-1);//用来承载结果，初始化一个大小为2，值为-1的容器b
        for(int i=0;i<nums.size();i++)
        {
            if(a.count(target-nums[i])>0)
            {
                b[0]=a[target-nums[i]];
                b[1]=i;
                break;
            }
            a[nums[i]]=i;//反过来放入map中，用来获取结果下标
        }
        return b;
    };
};

执行用时 :12 ms, 在所有 cpp 提交中击败了 87.61% 的用户
内存消耗 :10 MB, 在所有 cpp 提交中击败了 41.35% 的用户


