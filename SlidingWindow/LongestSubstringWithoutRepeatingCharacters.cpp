class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> seen = {};
        int start=0, end=0, count=0, maxCount=0;

        while(end < s.size()) {
            if(seen.find(s[end]) == seen.end()) {
                seen.insert(s[end]);
                count++;
            }

            else {
                while(s[start] != s[end]) {
                    seen.erase(s[start]);
                    count--;
                    start++;
                }
                if(s[start] == s[end]) {
                    start++;
                }
            }

            maxCount = max(maxCount, count);
            end++;
        }
        
        return maxCount;
    }
};