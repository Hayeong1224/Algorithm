#include<bits/stdc++.h>
using namespace std;

int pre[5001];
int nxt[5001];
vector<int> output;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K, len = 0;
    cin >> N >> K;

    for(int i=1; i<=N; i++){
        pre[i] = (i == 1)? N : i - 1;
        nxt[i] = (i == N)? 1 : i + 1;
        len++;
    }
    
    int cursor = 1;
    while(len != 0){
        if(cursor == 1) cursor = nxt[nxt[cursor]];
        else cursor = nxt[nxt[nxt[cursor]]];
        pre[nxt[cursor]] = pre[cursor];
        nxt[pre[cursor]] = nxt[cursor];
        output.push_back(cursor);
        len--;
    }

    cout << "<";
    for(int i=0; i<N; i++){
        if(i == N-1) cout << output[i] << ">\n";
        else cout << output[i] << ", ";
    }
}