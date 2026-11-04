# HackerRank - Find the Median
# Problem: Find the Median
# Source: https://www.hackerrank.com/challenges/find-the-median/problem
# Note: Returns the middle value of an odd-sized array after sorting, using Python's statistics module.
import statistics
def findMedian(arr):
    return statistics.median(arr)
