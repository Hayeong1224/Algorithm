#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.begin(), citations.end());
        
    int count=0;
    int num = 0;
    int i=0;
    
    while(1){
        count = 0;
        num++;
        for(auto c: citations)
            if(num <= c) count ++;
        if(count < num) break;
    }
    answer = num-1;
    
    return answer;
}