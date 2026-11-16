-- Problem: Two Sum
-- Source: https://leetcode.com/problems/calculate-digit-sum-of-a-string?envType=daily-question&envId=2026-11-16

-- Helper function to split a string into chunks of size k
chunksOf :: Int -> String -> [String]
chunksOf _ [] = []
chunksOf k s  = 
    let (h, t) = splitAt k s
    in h : chunksOf k t

-- Calculates the sum of digits of a single group and returns it as a String
sumGroupDigits :: String -> String
sumGroupDigits group = show (sum [fromEnum c - fromEnum '0' | c <- group])

-- Performs a single round of transformation
roundDigitSum :: Int -> String -> String
roundDigitSum k s = concatMap sumGroupDigits (chunksOf k s)

-- Main function that repeats the rounds until the length of s is <= k
digitSum :: String -> Int -> String
digitSum s k
    | length s <= k = s
    | otherwise     = digitSum (roundDigitSum k s) k