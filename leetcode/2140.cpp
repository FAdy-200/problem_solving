// https://leetcode.com/problems/solving-questions-with-brainpower/
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
private: 
    long long DB(int i,vector<vector<int>>& questions,vector<long long>& backtrack) {
        if(i >= questions.size()) return 0;
        if(backtrack[i]>=0) return backtrack[i];
        backtrack[i] = std::max(DB(i+1,questions,backtrack) ,DB(i + questions[i][1] + 1,questions,backtrack) + questions[i][0]);
        return backtrack[i];
    }
public:
    long long mostPoints(vector<vector<int>>& questions) {
        vector<long long> backtrack(questions.size() + 1,-1);
        return DB(0,questions,backtrack);
    }
};


int main(){
    Solution S;
    vector<vector<int>> questions = {{3,2},{4,3},{4,4},{2,5}};
    cout << S.mostPoints(questions) << endl;
    return 0;
}
