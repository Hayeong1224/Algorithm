#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tc;
    cin >> tc;

    while(tc--){
        string input;
        cin >> input;
        
        list<char> pw;
        auto cursor = pw.begin();
        for(auto c:input) {
            if(c == '<') {
                if(cursor != pw.begin()) cursor --;   
            }
            else if(c == '>') {
                if(cursor != pw.end()) cursor ++;
            }
            else if(c == '-') {
                if(cursor != pw.begin()){
                    cursor--;
                    cursor = pw.erase(cursor);
                } 
            }
            else pw.insert(cursor, c);
        }  
        
        for(auto i:pw) cout << i;
        cout << '\n';
    }
}