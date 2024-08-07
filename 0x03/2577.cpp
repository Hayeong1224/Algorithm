#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c;
    cin >> a >> b>> c;
    int mul = a*b*c;

    int count[10] = {};
    string s = to_string(mul);
    for(char c : s) count[c-'0'] ++;
    for(int i=0; i<10; i++) cout << count[i] << "\n";
}