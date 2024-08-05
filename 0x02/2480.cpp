#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int array[3];
    for(int i=0;i<3;i++) cin >> array[i];
    sort(array, array+3);
    if(array[0] == array[2]) cout << 10000 + array[0] * 1000;
    else if(array[0] == array[1] || array[1] == array[2]) cout << 1000 + array[1] * 100;
    else cout << array[2] * 100;
}