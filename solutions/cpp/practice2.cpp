// Problem: Valid Palindrome
// Source: https://leetcode.com/problems/valid-palindrome/
// Topic: Two Pointers, String

#include <iostream>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

bool isPalindrome(const string& s) {
    int left = 0;
    int right = static_cast<int>(s.length()) - 1;

    while (left < right) {
        while (left < right && !isalnum(static_cast<unsigned char>(s[left]))) {
            left++;
        }
        while (left < right && !isalnum(static_cast<unsigned char>(s[right]))) {
            right--;
        }

        if (tolower(static_cast<unsigned char>(s[left])) != tolower(static_cast<unsigned char>(s[right]))) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}

int main() {
    assert(isPalindrome("A man, a plan, a canal: Panama") == true);
    assert(isPalindrome("race a car") == false);
    assert(isPalindrome(" ") == true);
    assert(isPalindrome("0P") == false);

    cout << "All Valid Palindrome C++ test cases passed!" << endl;
    return 0;
}

