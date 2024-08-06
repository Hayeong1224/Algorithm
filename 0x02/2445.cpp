#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for(int i=1; i<2*n; i++){
        int idx;
        if(n<i) idx = 2*n-i;
        else idx = i;
        for(int j=1; j<=2*n; j++){
            if(idx<j && j <= 2*n-idx) cout << ' ';
            else cout << '*';
        }
        cout << "\n";
    }
}