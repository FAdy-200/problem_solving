// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <vector>
#include <unordered_map>
#include <math.h>
#include <algorithm>

using std::vector;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::max;
using std::sort;
using std::unordered_map;


class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int,int> dp;
        int ans = 0;
        for (int i = arr.size() - 1; i >=0; i--)
        {
            if(dp.find(arr[i] + difference) == dp.end()){
                dp[arr[i]] = 1;
            }else{
                dp[arr[i]] = dp[arr[i] + difference] + 1;
            }
            if(dp[arr[i]] > ans) ans = dp[arr[i]];

        }
        return ans;
    }
};

int main(){
    Solution S;
    vector<int> vals = {1,3,5,7};
    cout << S.longestSubsequence(vals,1) << endl;
    return 0;
}