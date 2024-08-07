#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    for(int i=0; i<N; i++){
        string s1, s2;
        cin >> s1 >> s2;

        int alp_s1[26]= {}, alp_s2[26] = {};
        for(char c : s1) alp_s1[c-'a']++;
        for(char c : s2) alp_s2[c-'a']++;
        bool isPossible = true;
        for(int i=0;i<26;i++) if(alp_s1[i]!=alp_s2[i]) isPossible = false;

        if(isPossible) cout << "Possible" << "\n";
        else cout << "Impossible" << "\n";
    }
}