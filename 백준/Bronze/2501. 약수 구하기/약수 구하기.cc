#include <iostream>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K; 
    int ct = 0;
    for(int i=N; i>0; i--) {
        if(N%i == 0) ct ++;
        if(ct == K) {
            cout << N/i;
            return 0;
        }
    }  
    cout << 0;
    return 0;
}