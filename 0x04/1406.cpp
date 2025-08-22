#include<bits/stdc++.h>
using namespace std;

string s = "";
int M;

int main(void) {
    cin >> s;
    list<char> lst(s.begin(),s.end());
    auto cursor = lst.end();

    cin >> M;
    char cmd, c;
    for(int i=0; i<M; i++) {
        cin >> cmd;

        if(cmd == 'L'){
            if(cursor != lst.begin()) cursor --;
        }else if(cmd == 'D'){
            if(cursor != lst.end()) cursor ++;
        }else if (cmd == 'B') {
            if(cursor != lst.begin()) cursor = lst.erase(--cursor);
        }else if (cmd == 'P'){
            cin >> c;
            lst.insert(cursor,c);
        }
    }

    for(auto c:lst) cout << c;
}