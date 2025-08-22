#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    stack<int> s;

    while(N-- > 0) {
        string cmd;
        int num;
        cin >> cmd;
        if(cmd == "push") {
            cin >> num;
            s.push(num);
        }else if(cmd == "pop") {
            if(s.empty()) cout << -1 << '\n';
            else {
                cout << s.top() << '\n';
                s.pop();
            }
        }else if(cmd == "size") {
            cout << s.size() << '\n';
        }else if(cmd == "empty") {
            cout << s.empty() << '\n';
        }else if(cmd == "top") {
            if(s.empty()) cout << -1 << '\n';
            else {
                cout << s.top() << '\n';
            }
        }
    }
}