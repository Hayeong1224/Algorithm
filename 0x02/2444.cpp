#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for(int i=1;i<=2*n-1;i++){
        int idx;
        if(n<i) idx = 2*n-i; //i>n case
        else idx = i;
        for(int j=1; j<=2*n-1; j++){
            if(j <= n-idx) cout << ' ';
            else if(n-idx < j && j < n+idx) cout << '*';
            else break;
        }
        cout << "\n";
    }
}