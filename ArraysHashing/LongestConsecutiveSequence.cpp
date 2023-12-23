class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set;

        // add all elements of nums to set
        for(int num: nums) {
            set.insert(num);
        }

        // initializing maxVal
        int maxVal = 0;

        // iterate over nums array
        for(int num: nums) {
            // check if it is the smallest element of series
            if(set.find(num-1) == set.end()) { // check if no value found
                int j=0, count=0;
                cout<<num+j;
                while(set.find(num+j) != set.end()) {
                    j++;
                    count++;
                }
                if(count>maxVal) maxVal = count;
            }
        }

        return maxVal;
    }
};