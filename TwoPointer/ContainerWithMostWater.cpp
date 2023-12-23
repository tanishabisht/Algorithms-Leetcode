class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0;
        int j=height.size()-1;

        int maxArea = 0;

        while(i<j) {
            int w = j - i;
            int h = min(height[i], height[j]);
            if(h*w > maxArea) maxArea = h * w;

            if(height[i] < height[j]) i++;
            else if(height[i] > height[j]) j--;
            else i++;
        }
        
        return maxArea;
    }
};