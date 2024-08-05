#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int input, odd_sum = 0, odd_min = 100;
    for(int i=0; i<7; i++)
    {
        cin >> input;
        if(input & 1)
        {
            odd_sum += input;
            if(odd_min > input) odd_min = input;
        }
    }
    if(odd_sum > 0) cout << odd_sum << '\n' << odd_min;
    else cout << -1;
}  