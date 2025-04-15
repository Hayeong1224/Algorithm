#include <iostream>
using namespace std;

int main(void) {
    int max = 0, ct = 0;
    int out, in;
    for(int i=0;i<10;i++) {
        cin >> out >> in;
        ct = ct - out + in;
        if(ct > max) max = ct;
    }
    cout << max;
}

