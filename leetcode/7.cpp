// https://leetcode.com/problems/reverse-integer/description/
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
    int reverse(int x) {
        vector<int> MINT = {2,1,4,7,4,8,3,6,4,8};
        vector<int> num;
        if(x<0)MINT[9] = 8;
        long int tx = abs(x);
        while(tx){
            num.push_back(tx%10);
            tx = tx/10;
        }
        int n = num.size();
        int ans = 0;
        if(n == MINT.size()){
            for (int i = 0; i < n; i++)
            {
                if(abs(num[i])<MINT[i])break;
                if(abs(num[i])>MINT[i])return 0;
            }
            
        }
        for (int i = 0; i < n; i++)
        {
            ans += num[i] * (pow(10,n-i-1));
            
        }
        
        if(x<0)ans*=-1;
        return ans;
    }
};


int main(){
    Solution S;
    cout << S.reverse(-2147483648) << endl;
    return 0;
}