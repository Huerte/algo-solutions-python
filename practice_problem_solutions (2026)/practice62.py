# Number of Employees Who Met the Target

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return sum(1 for i in hours if i >= target)

