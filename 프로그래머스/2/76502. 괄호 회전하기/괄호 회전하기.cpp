#include <bits/stdc++.h>

using namespace std;

unordered_map<char, char> bracketPair = {{')','('}, {']','['}, {'}', '{'}};

int solution(string s) {
    int answer = 0;
    unsigned int n=s.size();
    
    for(int i=0;i<n; i++){ //전체 회전
        stack<char> st;
        bool isWrong = false;
        for(int j=0; j<n; j++){ //각 회전 별 문자 체크
            char c = s[(i+j)%n];
            if(bracketPair.count(c)){//닫힌 괄호
                if(st.empty() || st.top() != bracketPair[c]) {
                    isWrong = true;
                    break;
                }
                else st.pop();
            } else st.push(c); //열린 괄호
        }
        if(!isWrong && st.empty()) answer++;
    }
    return answer;
}