#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max_x = 0; // x를 긴 걸로 몰기
    int max_y = 0;
    for(const auto& pair: sizes) {
        auto x = pair[0];
        auto y = pair[1];
        
        if (x>y) {
            if (max_x < x) max_x = x;
            if (max_y < y) max_y = y;
        }
        else {
            if (max_x < y) max_x = y;
            if (max_y < x) max_y = x;
        }
    } 
    return max_x * max_y;
}