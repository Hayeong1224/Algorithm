#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int M, N;
    cin >> M >> N;
    vector<int> v;
    for(auto i=M; i<=N; i++) {
        if(i==1) continue;
        v.push_back(i);
        for(int j=2; j<i; j++) {
            if(i%j==0) {
                v.pop_back();
                break;
            }
        }
    }

    if(!v.empty()){
        sort(v.begin(), v.end());
        auto sum = 0;
        for (int value : v)
            sum += value;
        cout << sum << '\n' << v[0];
    } else cout << -1;
}