// Problem: Merge Intervals
// Source: https://leetcode.com/problems/merge-intervals/
// Topic: Arrays, Sorting
// Status: IN PROGRESS

function merge(intervals) {
  if (intervals.length <= 1) {
    return intervals;
  }

  intervals.sort((a, b) => a[0] - b[0]);
  const merged = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const current = intervals[i];
    const last = merged[merged.length - 1];

    if (current[0] <= last[1]) {
      last[1] = current[1];
    } else {
      merged.push(current);
    }
  }

  return merged;
}

const out1 = merge([[1, 3], [2, 6], [8, 10], [15, 18]]);
console.assert(JSON.stringify(out1) === JSON.stringify([[1, 6], [8, 10], [15, 18]]), "Test 1 failed");

const out2 = merge([[1, 4], [4, 5]]);
console.assert(JSON.stringify(out2) === JSON.stringify([[1, 5]]), "Test 2 failed");

const out3 = merge([[1, 4], [2, 3]]);
console.assert(JSON.stringify(out3) === JSON.stringify([[1, 4]]), "Test 3 failed");

