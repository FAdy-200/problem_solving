// https://leetcode.com/problems/max-area-of-island/
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
private:
    int crawl(int i,int j,vector<vector<int>>& grid){
        int ans = 1;
        grid[i][j] = 0;
        if(i>0 && grid[i-1][j]) ans +=crawl(i-1,j,grid);
        if(i<grid.size() - 1 &&grid[i+1][j]) ans +=crawl(i+1,j,grid);
        if(j>0 && grid[i][j-1]) ans +=crawl(i,j-1,grid);
        if(j<grid[0].size() - 1 && grid[i][j+1]) ans +=crawl(i,j+1,grid);
        return ans;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if(grid[i][j]) ans = max(ans,crawl(i,j,grid));
            }
            
        }
        return ans;
    }
};

int main(){
    Solution S;
    vector<vector<int>> grid = {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                {0,1,1,0,1,0,0,0,0,0,0,0,0},
                                {0,1,0,0,1,1,0,0,1,0,1,0,0},
                                {0,1,0,0,1,1,0,0,1,1,1,0,0},
                                {0,0,0,0,0,0,0,0,0,0,1,0,0},
                                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                {0,0,0,0,0,0,0,1,1,0,0,0,0}};
    cout << S.maxAreaOfIsland(grid) << endl;
    return 0;
}