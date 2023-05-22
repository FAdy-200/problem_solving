// https://leetcode.com/problems/coin-change-ii/
#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <vector>
#include <unordered_map>
#include <math.h>

using std::vector;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::max;

class Solution {

public:
    int change(int amount, vector<int>& coins) {
        vector<int> seen(amount+1,0);
        seen[0] = 1;
        for (auto &&i : coins)
        {
            for (int j = 1; j < amount+1; j++)
            {
                if(j-i >= 0)seen[j]+= seen[j-i];
            }
            
        }
        return seen[amount];
        
    }
};

int main(){
    Solution S;
    vector<int> coins = {1,2,5};
    cout << S.change(5,coins) << endl;
    return 0;
}