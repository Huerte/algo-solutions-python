// Problem: Search in Rotated Sorted Array
// Source: https://leetcode.com/problems/search-in-rotated-sorted-array/
// Topic: Binary Search, Arrays
// Status: IN PROGRESS

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int search(const vector<int>& nums, int target) {
    int low = 0;
    int high = static_cast<int>(nums.size()) - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (nums[mid] == target) {
            return mid;
        }

        if (nums[low] < nums[mid]) {
            if (target >= nums[low] && target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else {
            if (target > nums[mid] && target <= nums[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }

    return -1;
}

int main() {
    assert(search({4, 5, 6, 7, 0, 1, 2}, 0) == 4);
    assert(search({4, 5, 6, 7, 0, 1, 2}, 3) == -1);
    assert(search({1}, 0) == -1);
    assert(search({3, 1}, 1) == 1);

    return 0;
}

