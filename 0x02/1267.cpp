#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num;
    cin >> num;

    int time[num];
    for(int i=0;i<num;i++) cin >> time[i];
    
    int ys = 0, ms = 0;
    for(int i=0;i<num;i++)
    {
        ys += (time[i]/30+1) * 10;
        ms += (time[i]/60+1) * 15;
    }

    if(ys<ms) cout << "Y" << " " << ys;
    else if(ms<ys) cout << "M" << " " << ms;
    else cout << "Y M" << " " << ys;
}