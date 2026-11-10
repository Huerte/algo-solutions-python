// Problem: Two Sum
// Source: https://leetcode.com/problems/two-sum/
// Note: Uses an unordered_map for efficient O(n) lookup.

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> seen;

    for (int i = 0; i < static_cast<int>(nums.size()); i++) {
        int complement = target - nums[i];

        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }

        seen[nums[i]] = i;
    }

    return {};
}

int main() {
    vector<int> result1 = twoSum({2, 7, 11, 15}, 9);
    vector<int> result2 = twoSum({3, 2, 4}, 6);
    vector<int> result3 = twoSum({3, 3}, 6);

    for (const auto& result : {result1, result2, result3}) {
        cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    }

    return 0;
}
