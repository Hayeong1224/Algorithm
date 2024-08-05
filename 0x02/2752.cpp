#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    /*
    //use min(), max()
    int a, b, c;
    cin >> a >> b >> c;
    
    int d, e, f;
    d = min({a, b, c});
    f = max({a, b, c});
    e = a+b+c-d-f;
    cout << d << ' ' << e << ' ' << f;
    */

    //use sort()
    int array[3];
    for(int i=0; i<3; i++)
    {
        cin >> array[i];
    }
    sort(array, array+3);
    for(int i=0; i<3; i++)
    {
        cout << array[i] << " ";
    }
}