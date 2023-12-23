class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        set<vector<int>> set;
        vector<vector<int>> ans;

        int n = nums.size();

        for(int i=0; i<nums.size(); i++) {
            int j = i+1;
            int k = n-1;

            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if(sum < 0) j++;
                else if(sum > 0) k--;
                else {
                    set.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                }
            }
        }

        for (auto s: set) {
            ans.push_back(s);
        }

        return ans;
    }
};