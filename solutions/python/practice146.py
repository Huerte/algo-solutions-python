# Number of Employees Who Met the Target
# Problem: Number of Employees Who Met the Target
# Source: https://leetcode.com/problems/number-of-employees-who-met-the-target/
# Note: Counts employees whose working hours are greater than or equal to the target.

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return sum(1 for i in hours if i >= target)

