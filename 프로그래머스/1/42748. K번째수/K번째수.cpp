#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (const auto& com : commands) {
        int i = com[0], j = com[1], k = com[2];
        vector<int> temp(array.begin() + i-1, array.begin() + j);
        sort(temp.begin(), temp.end());
        answer.push_back(temp[k - 1]);
    }
        
    
    return answer;
}