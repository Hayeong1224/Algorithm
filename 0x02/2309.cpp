#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int input[9], result[7];
    int sum = 0;
    for(int i=0;i<9;i++)
    {
        cin >> input[i];
        sum += input[i];
    } 
    for(int i=0;i<8;i++)
    {
        for(int j=i+1;j<9;j++)
        {   //7명 찾기
            if(sum - input[i] - input[j] == 100)
            {
                for(int k=0, idx = 0; k<9; k++) if(k != i && k != j) result[idx++] = input[k];
                break;
            }
        }
    }
    sort(result, result+7);
    for(int i=0;i<7;i++) cout << result[i] << '\n';
}