#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <vector>


using std::vector;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::max;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* thead = head;
        int n=0;
        while(thead){
            n++;
            thead = thead->next;
        }
        int half = (int) n/2;
        int stack[half];
        int ans = 0;
        int i = 0,j = half-1;
        thead = head;
        while(thead){
            if(i<half){
                stack[i++] = thead->val;
            }else{
                ans = max(ans,stack[j--]+thead->val);
            }
            thead = thead->next;
        }
        return ans;
    }
};