class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;
        for(int i=0; i<nums.size(); i++){
            int look = target - nums[i];
            if(seen.count(look) == 0) {
                seen[nums[i]] = i;
            } else {
                return { i, seen[look]};
            }
        }
        return { 0, 0 };
    }
};