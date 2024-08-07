#include<bits/stdc++.h>
using namespace std;

int freq[26]; //0으로 자동 초기화
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    // a~z: 92 ~ 122 -> a:0 으로 만드려면 a를 빼주면 됨!
    for(char c : s) freq[c-'a']++;
    for(int i=0; i<26; i++) cout << freq[i] << ' ';
}