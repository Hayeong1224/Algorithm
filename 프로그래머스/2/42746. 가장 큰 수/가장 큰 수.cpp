#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool compare(string a, string b){
    return a+b > b+a;
}

string solution(vector<int> numbers) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector<string> tmp;
    string answer = "";
    
    for(auto num :numbers)
        tmp.push_back(to_string(num));
    sort(tmp.begin(), tmp.end(), compare);
    for(auto a:tmp)
        answer += a;
    if(answer[0] == '0') answer = "0";
    return answer;
}