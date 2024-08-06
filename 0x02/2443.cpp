#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for(int i=n; i>0; i--){
        for(int j=1; j<=2*n-1; j++){
            if(j<=n-i) cout << ' ';
            else if(n-i < j && j < n+i) cout << '*';
            else break;
        }
        cout << "\n";
    }
}