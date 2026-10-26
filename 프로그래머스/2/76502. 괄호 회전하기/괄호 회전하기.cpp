#include <string>
#include <vector>
#include <stack>
#include <unordered_map>

using namespace std;

int is_right(string s) {
    int n = s.length();
    
    stack<char> st;
    unordered_map<char, char> um = {
        {']', '['},
        {'}', '{'},
        {')', '('}
    };
    
    for (char ch : s) {
        if (!um.count(ch)) st.push(ch);
        else{
            if(st.empty() || st.top() != um[ch]) return 0;
            st.pop();
        }
    }
    
    if (st.empty()) return 1;
    else return 0;
}

int solution(string s) {
    int answer = 0;
    int n = s.length();
    
    for (int i=0; i<n; i++) {
        answer += is_right(s.substr(i) + s.substr(0,i));
    }
    
    return answer;
}