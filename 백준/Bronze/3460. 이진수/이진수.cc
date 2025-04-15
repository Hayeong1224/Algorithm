#include <iostream>

using namespace std;

int main() {
    
    unsigned int n, tc;
    cin >> tc;
    while(tc-->0) {
        cin >> n;
        for(int i=0; i<21; i++){ //n<=10^6
            if((n&(1<<i)) > 0) cout << i << " ";
        }
    } 
    return 0;
}