#include<bits/stdc++.h>
using namespace std;

// 각 자연수의 존재 여부를 저장하는 배열, 아래에서 x-arr[i]가 1000000보다 큰 경우를 예외처리하기 싫어서 그냥 배열을 최대 200만으로 잡음
int num[2000001];
int arr[1000001];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x, cnt = 0;
    cin >> n;

    for(int i=0;i<n;i++) cin >> arr[i];
    cin >> x;
    for(int i=0;i<n;i++){
        if(x-arr[i] > 0 && num[x-arr[i]]) cnt ++;
        else num[arr[i]]++;
    }
    cout << cnt;
}