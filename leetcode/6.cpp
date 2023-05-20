// https://leetcode.com/problems/zigzag-conversion/description/
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
    string convert(string s, int numRows) {
        if (numRows == 1)
        {
            return s;
        }
        
        vector<string> ans(numRows);
        int j = 0;
        int state = 1;
        for (int i = 0; i < s.size(); i++)
        {
            ans[j].push_back(s[i]);
            if(state > 0){
                if(++j == numRows - 1) state*=-1;
            }else{
                if(++j == 0) state*=-1;
            }
        }
        string out;
        for (auto &&i : ans)
        {
            out.append(i);
        }
        
        return out;
    }

};


int main(){
    Solution S;
    cout << S.convert("PAYPALISHIRING",4) << endl;
    return 0;
}