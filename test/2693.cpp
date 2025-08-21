#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int T, temp;
    cin >> T;
    vector<int> A;
    while(T-- > 0){
        for (int i = 0; i < 10; i++) {
            cin >> temp;
            A.push_back(temp);
        }
        sort(A.begin(), A.end());
        cout << A[7] << '\n';
        A.clear();
    }
}