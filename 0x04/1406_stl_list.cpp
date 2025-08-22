#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string init;
    cin >> init;
    list<char> l;
    for(auto c: init) l.push_back(c);
    auto cursor = l.end();

    int M;
    cin >> M;
    while(M--){
        char op;
        cin >> op;
        if(op == 'P'){
            char input;
            cin >> input;
            l.insert(cursor, input);
        }
        else if(op == 'B'){
            if(cursor != l.begin()){
                cursor--;
                cursor = l.erase(cursor);
            }
        }
        else if(op == 'D'){
            if(cursor != l.end()) cursor++;
        }
        else if (op == 'L'){
            if(cursor != l.begin()) cursor--;
        }
    }
    cursor = l.begin();
    for(auto i : l) cout << i;
}