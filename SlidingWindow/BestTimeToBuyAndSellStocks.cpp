class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i=0, j=1, maxProfit=0;
        while(i<j && j<prices.size()) {
            if(prices[i] >= prices[j]) {
                if(j == i+1) {
                    i++;
                    j++;
                } else {
                    i++;
                }
            }
            else if(prices[j] > prices[i]) {
                maxProfit = max(maxProfit, prices[j]-prices[i]);
                j++;
            }
        }
        return maxProfit;
    }
};