// https://leetcode.com/problems/powx-n/description/
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
using std::unordered_map;

class Solution {
private:
    double powHelper(double x, long int n, unordered_map<long, double>& seen){
        if (seen.find(n) == seen.end()){
            // if(n==1) return x;
            double first = powHelper(x,(int) (n/2),seen);
            double sec = powHelper(x,n - ((int) (n/2)),seen);
            // return powHelper(x,(int) (n/2)) * powHelper(x,n - ((int) (n/2)));
            seen[n] = first * sec;
            // return seen[n];
        } return seen[n];

    }
public:
    double myPow(double x, int n) {
        unordered_map<long int, double> seen;
        long int nn = (long int) n;
        if (n == 0) return 1;
        if(n < 0){
            seen[1] = x;
            return 1/powHelper(x,-nn,seen);
        }
        seen[1] = x;
        return powHelper(x,nn,seen);
    }
};

int main(){
    Solution S;
    cout << S.myPow(1.0,-2147483648) << endl;
    return 0;
}