#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for(int i=n;i>0;i--){
        for(int j=n;j>0;j--){
            if(i>=j) cout << '*';
            else cout << ' ';
        }
        cout << "\n";
    } 
}