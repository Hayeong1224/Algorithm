#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long a, b, ab_min, ab_max, num;
    cin >> a >> b;
    ab_min = min(a,b);
    ab_max = max(a,b);
    num = ab_max - ab_min - 1;
    if(num < 0) num = 0;
    cout << num << '\n';
    for(long long i=1; num > 0; num--) cout << ab_min + (i++) << ' ';
}