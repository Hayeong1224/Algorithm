#include<bits/stdc++.h>
using namespace std;

int alp_s1[26];
int alp_s2[26];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s1, s2;
    cin >> s1 >> s2;

    for(auto c : s1) alp_s1[c-'a']++;/
    for(auto c : s2) alp_s2[c-'a']++;

    int cnt = 0;
    for(int i=0;i<26;i++) cnt += abs(alp_s1[i] -alp_s2[i]);
    cout << cnt;
}