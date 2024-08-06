#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // 전역변수의 초기값은 0.
    // 초기화하기 싷으면 전역변수로 하기.
    int input, max=0, max_idx;
    for(int i=1; i<=9; i++){
        cin >> input;
        if(max < input){
            max = input;
            max_idx = i;
        } 
    }
    cout << max << "\n" << max_idx;
}