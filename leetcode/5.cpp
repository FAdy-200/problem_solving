// https://leetcode.com/problems/longest-palindromic-substring/description/
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
// TODO: finish this
class Solution {
private:
    vector<int> DB(string& s,int i, int j,vector<vector<vector<int>>>& seen){
        if(i==j) return {i,j};
        if(seen[i][j][0]>=0) return seen[i][j];
        string ns = s.substr(i,j-i+1);
        string rns = string(ns.rbegin(),ns.rend());
        if(ns == rns) {
            seen[i][j] = {i,j};
            return {i,j};
        }
        vector<int> t1 = DB(s,i+1,j,seen), t2 = DB(s,i,j-1,seen);
        if((t1[1]-t1[0])>(t2[1]-t2[0])) {
            seen[i][j] = t1;
            return t1;
        }
        seen[i][j] = t2;
        return t2;
    }
private:
    string DB2(string s,unordered_map<string,string>& seen){
        if (seen.find(s) == seen.end()){
            string ns = string(s.rbegin(),s.rend());
            if(ns == s){
                seen[s] = s;
                return s;
            }
            string t1 = DB2(s.substr(1),seen), t2 = DB2(s.substr(0,s.size()-1),seen);
            if(t1.size()>t2.size()){
                seen[s] = t1;
                return t1;
            }
            seen[s] = t2;
            return t2;
            
        } return seen[s];
    }
public:
    string longestPalindrome(string s) {
        vector<vector<vector<int>>> seen(s.size()+1,vector<vector<int>> (s.size()+1,{-1,-1}));
        vector<int> ans = DB(s,0,s.size(),seen);
        return s.substr(ans[0],ans[1]);
        // unordered_map<string,string> seen;
        // seen[""] = "";
        // return DB2(s,seen);
    }
};

int main(){
    Solution S;
    cout << S.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv") << endl;
    // cout << S.longestPalindrome("bacabab") << endl;
    return 0;
}