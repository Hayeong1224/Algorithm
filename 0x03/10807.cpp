#include<bits/stdc++.h>
using namespace std;

int arr[201];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, input, v;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> input;
        arr[input+100]++; 
    }
    cin >> v;
    cout << arr[v+100];
}