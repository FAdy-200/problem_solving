// https://leetcode.com/problems/spiral-matrix-ii/
#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <vector>

using std::vector;
using std::cout;
using std::cin;
using std::endl;
using std::string;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n,vector<int> (n));
        int i = 0,j = 0,state = 0;
        int end = n; // end of move
        // state = 0,1,2,3
        for (int m = 1 ;m < (n*n + 1); m++){
            ans[i][j] = m;
            switch (state){
                case 0: // moving right
                    if(j == end-1){
                        i++;
                        state = 1;
                    }else{
                        j++;
                    }
                    break;
                case 1: // moving down
                    if(i == end-1){
                        j--;
                        state = 2;
                    }else{
                        i++;
                    }
                    break;
                case 2: // moving left
                    if(j == n-end){
                        i--;
                        state = 3;
                        end--;
                    }else{
                        j--;
                    }
                    break;
                default: // moving up
                    if(i == n-end){
                        j++;
                        state = 0;
                    }else{
                        i--;
                    }
                    break;
            }

        }
        return ans;
    }
};

int main(){
    Solution S;
    S.generateMatrix(4);
    return 0;
}
