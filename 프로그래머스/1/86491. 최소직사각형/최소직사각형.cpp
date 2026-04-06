#include <string>
#include <vector>
using namespace std;

int solution(vector<vector<int>> sizes) {
    int mw = 0;
    int mh = 0;
    for (auto s : sizes) {
        mw = max(mw, max(s[0], s[1]));
        mh = max(mh, min(s[0], s[1]));
    }
    return mw * mh;
}