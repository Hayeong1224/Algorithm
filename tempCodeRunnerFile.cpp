#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    float a;

    cin >> a;

    float result;

    result = sqrt(a);
    result = floor(100 * result) /100;

    cout << result << endl;

    return 0;
}
