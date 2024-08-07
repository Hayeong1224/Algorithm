#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num[10] = {};
    int cnt = 0, input;

    cin >> input;

    //자리수로 풀기
    while(input){
        int idx = input%10;
        if(num[idx]==0){
            if(idx==6 && num[9]>0) num[9]--;
            else if(idx==9 && num[6]>0) num[6]--;
            else{
                for(int i=0;i<10;i++) num[i]++;
                cnt++;
                num[idx]--;
            }
        }
        else num[idx]--;
        input /= 10;
    }

    /*
    //string으로 풀기
    string s = to_string(input);
    for(char c : s){
        if(num[c-'0'] == 0){
            if(c-'0' == 6 && num[9] > 0) num[9]--;
            else if(c-'0' == 9 && num[6] > 0) num[6]--;
            else{
                cnt ++;
                for(int i=0; i<10; i++) num[i] ++;
                num[c-'0'] --;
            }
        }
        else num[c-'0'] --;
    }
    */
    cout << cnt;
}