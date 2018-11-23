//
// Created by gz on 18-11-21.
//
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
//        int rows = matrix.size();
//        int cols = matrix[0].size();
        if (!matrix.empty()) {
            int row = 0;
            int column = matrix[0].size() - 1;
            while (row < matrix.size() && column >= 0){
                if (target == matrix[row][column])
                    return true;
                else if (target < matrix[row][column])
                    --column;
                else
                    ++row;
            }
        }
        return false;
    }
};

int main(){
//    vector<vector<int>> matrix = {
//            {1,   3,  5,  7},
//            {10, 11, 16, 20},
//            {23, 30, 34, 50}
//    };
//    int target = 1;
//    Solution sol;
//    cout << boolalpha << sol.searchMatrix(matrix, target) << endl;
    vector<vector<int>> matrix = {
    };
    int target = -1;
    Solution sol;
    cout << boolalpha << sol.searchMatrix(matrix, target) << endl;
    return 0;
}