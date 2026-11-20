// Problem: Move Zeroes
// Source: https://leetcode.com/problems/move-zeroes/
// Topic: Two Pointers, Arrays
// Status: IN PROGRESS

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

void moveZeroes(vector<int>& nums) {
    int insertPos = 0;

    for (int i = 0; i < static_cast<int>(nums.size()); i++) {
        if (nums[i] != 0) {
            nums[insertPos++] = nums[i];
        }
    }

    for (int i = insertPos + 1; i < static_cast<int>(nums.size()); i++) {
        nums[i] = 0;
    }
}

int main() {
    vector<int> nums1 = {0, 1, 0, 3, 12};
    moveZeroes(nums1);
    assert((nums1 == vector<int>{1, 3, 12, 0, 0}));

    vector<int> nums2 = {0};
    moveZeroes(nums2);
    assert((nums2 == vector<int>{0}));

    return 0;
}

