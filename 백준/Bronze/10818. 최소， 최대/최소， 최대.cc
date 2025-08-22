#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    long N, temp;

    cin >> N;
    vector<long> v;
    while(N--){
        cin >> temp; //-10^6 <= temp <= 10^6
        v.push_back(temp); 
    }
    cout << *min_element(v.begin(), v.end()) << " " << *max_element(v.begin(), v.end());

    return 0;
}