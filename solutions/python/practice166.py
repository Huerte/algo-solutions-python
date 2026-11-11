# Problem: Display the First Three Rows
# Source: https://leetcode.com/problems/display-the-first-three-rows/
# Note: Returns the first three rows of the employees DataFrame using Pandas iloc

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]
