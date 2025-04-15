#include <iostream>
using namespace std;

int p, pp, result, n;
int main(void) {
    cin >> n;
    for(int i=0; i<=n; i++) {
        if(i==0) result = 0;
        else if(i==1) {
            p = result;
            result = 1;
        }
        else {
            pp = p;
            p = result;
            result = pp + p;
        }
    }
    cout << result;
}