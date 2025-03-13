#include<iostream>

using namespace std;

int main(){
    int numChickens, numCoke, numBeer;

    cin >> numChickens >> numCoke >> numBeer;

    // calculation (chi 1 - coke 2 / beer 1)

    int num = 0;
    while(num < numChickens && numCoke > 1){
        numCoke -= 2;
        num++;
    }
    while (num < numChickens && numBeer > 0)
    {
        numBeer -= 1;
        num++;
    }
    cout << num;
}