#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string a;
    cin >> a;
    
    int cnt = 0;
    stack<char> s;
    for(int i=0;i<a.length();i++){
        if(a[i] == '(') {
            if(a[i+1] == ')') { //레이저 
                if(!s.empty()) cnt += s.size();
                i++;
            } else s.push('('); //쇠막대기 시작
        } else {
                cnt++; //쇠막대기 끝
                s.pop();
            }
    }
    cout << cnt << '\n';
}