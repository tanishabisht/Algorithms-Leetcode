// SORTING
std::sort(nums.begin(), nums.end()); // increasing
std::sort(nums.begin(), nums.end(), greater <>()); // descreaing


// SET
unordered_set<int> op;
nums_set.insert(i); // add element


// FOR LOOP
// === 1: normal
for(int i=0; i < nums.size() - 1; i++) {}
// === 2: auto
for (auto & num : nums)  {}
// === 3: iterator
for(iter; iter < vec.end(); iter++)