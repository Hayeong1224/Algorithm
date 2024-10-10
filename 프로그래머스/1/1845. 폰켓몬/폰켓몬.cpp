#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> nums)
{
    unordered_set<int> uNum(nums.begin(), nums.end());
    
    return min(uNum.size(), nums.size()/2);
}