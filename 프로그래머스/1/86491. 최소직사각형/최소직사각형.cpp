#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_x = 0; // x를 긴 걸로 몰기
    int max_y = 0;
    for(const auto& pair: sizes) {
        max_x = max(max_x, max(pair[0], pair[1]));
        max_y = max(max_y, min(pair[0], pair[1]));
    } 
    return max_x * max_y;
}