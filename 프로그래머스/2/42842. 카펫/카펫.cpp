#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int rc = brown + yellow;
    
    for (int r = 3; r <= sqrt(rc); r ++) {
        if (rc % r == 0) {
            int c = rc / r;
            
            if ((r-2) * (c-2) == yellow) return {c,r};
        }
    }
}