#include <iostream>
using namespace std;

int main(void) {
    int A, B, i = 1, sum = 0, cnt = 1;
    cin >> A >> B;
    int a[1000];
    while (1){
        for(int j=0; j<i; j++){
            sum += i;
            a[cnt] = sum;
            if(++cnt > B) {
                cout << a[B] - a[A - 1];
                return 0;
            }
        }
        i++; 
    }
}