// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <vector>
#include <unordered_map>
#include <math.h>
#include<algorithm>

using std::vector;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::max;
using std::sort;

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(),piles.end(), [](int &a, int &b){ return a>b; });
        int ans = 0;
        for (int i = 0; i < piles.size() - (int)piles.size()/3; i+=2)
        {
            ans += piles[i];
        }
        return ans;
    }
};