// Problem: Invert Binary Tree
// Source: https://leetcode.com/problems/invert-binary-tree/
// Topic: Tree, Recursion

#include <iostream>
#include <cassert>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    TreeNode* temp = root->left;
    root->left = invertTree(root->right);
    root->right = invertTree(temp);

    return root;
}

int main() {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(7);

    TreeNode* inverted = invertTree(root);

    assert(inverted != nullptr);
    assert(inverted->val == 4);
    assert(inverted->left->val == 7);
    assert(inverted->right->val == 2);

    cout << "All Invert Binary Tree C++ test cases passed!" << endl;
    return 0;
}

