// https://leetcode.com/problems/house-robber/
#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <vector>
#include <unordered_map>

using std::vector;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::max;


class Solution {
public:
    int rob2(vector<int>& nums) {
        vector<int> taken;
        vector<int> notTaken;
        taken.push_back(nums[0]);
        notTaken.push_back(0);
        int temp;
        for (int i = 1 ;i < nums.size(); i++){
            temp = (max(notTaken.back()+nums[i],taken.back()));
            notTaken.push_back(max(taken.back(),notTaken.back()));
            taken.push_back(temp);
        }
        return max(taken.back(),notTaken.back());
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        int taken[n];
        int notTaken[n];
        taken[0] = nums[0];
        notTaken[0] = 0;
        int temp;
        for (int i = 1 ;i < n; i++){
            taken[i] = max(notTaken[i-1]+nums[i],taken[i-1]);
            notTaken[i] = max(taken[i-1],notTaken[i-1]);
        }
        return max(taken[n-1],notTaken[n-1]);
    }
};

int main(){
    Solution S;
    vector<int> vals = {2,7,9,3,1};
    cout << S.rob(vals) << endl;
    return 0;
}