// https://leetcode.com/problems/knight-dialer/
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
using std::unordered_map;


vector<unordered_map<int,int>> seen(11,unordered_map<int,int>());

class Solution {
private:
    int MOD = 1000000007;
private:
    int DB(int on,int n,unordered_map<int,vector<int>>& Dials,vector<unordered_map<int,int>>& seen){
        if (seen[on].find(n) == seen[on].end()){
            if(!n){
                seen[on][n] = 1;
                return 1;
            }
            int ans = 0;
            for (auto &&i : Dials[on])
            {
                ans = (ans + DB(i,n-1,Dials,seen))%MOD;
            }
            seen[on][n] = ans%MOD;
        }return seen[on][n];
    }
public:
    int knightDialer(int n) {
        unordered_map<int,vector<int>> Dials={
            {10,{0,1,2,3,4,5,6,7,8,9}},
            {0,{4,6}},
            {1,{6,8}},
            {2,{7,9}},
            {3,{4,8}},
            {4,{0,3,9}},
            {5,{}},
            {6,{0,1,7}},
            {7,{2,6}},
            {8,{1,3}},
            {9,{2,4}},
        };
        return DB(10,n,Dials,seen);
    }
};


int main(){
    Solution S;
    cout << S.knightDialer(2) << endl;
    return 0;
}