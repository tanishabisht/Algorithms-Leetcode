class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for(int i=0; i<strs.size(); i++) {
            string new_str = strs[i];
            sort(new_str.begin(), new_str.end());
            groups[new_str].push_back(strs[i]);
        }
        vector<vector<string>> ans;
        for (auto const& grp : groups) {
            ans.push_back(grp.second);
        }
        return ans;
    }
};