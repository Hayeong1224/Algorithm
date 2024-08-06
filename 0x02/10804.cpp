#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int cards[21];
    for(int i=1; i<=20; i++) cards[i] = i;
    int f,l;
    for(int i=1; i<=10; i++)
    {
        cin >> f >> l;
        //include first, exclude last
        //지금 0 -> 1이니까 5를 받으면 6이 나옴
        //reverse(cards+f-1, cards+l);
        //생각하기 싫으면 그냥 1 -> 1 넣고 0 값 쓰지 말기
        reverse(cards+f, cards+l+1);
    }
    for(int i=1; i<=20; i++) cout << cards[i] << " ";  
}