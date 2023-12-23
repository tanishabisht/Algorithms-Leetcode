class Solution {
public:

    static bool sortbysec(const tuple<int, int>& a, const tuple<int, int>& b) { 
        return (get<1>(a) < get<1>(b)); 
    } 

    vector<int> topKFrequent(vector<int>& nums, int k) {


        unordered_map<int,int> mp;
        for(auto num: nums) {
            mp[num]++;
        }


        vector<pair<int,int>> res;
        for(auto m: mp) {
            res.push_back({m.first, m.second});
        }
        sort(res.begin(), res.end(), sortbysec);


        vector<int> ans;
        for(auto r: res) {
            ans.push_back(r.first);
        }

        return vector<int>(ans.end()-k, ans.end());
    }
};