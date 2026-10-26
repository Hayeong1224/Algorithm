#include <string>
#include <vector>

using namespace std;

int dfs(const vector<int>& numbers, const int& target, int cur, int temp_sum) {
    if (cur == numbers.size()) {
        if (temp_sum == target) return 1;
        else return 0;
    }
    
    int result = 0;
    
    // 더하기
    result += dfs(numbers, target, cur+1, temp_sum + numbers[cur]);
    
    // 빼기
    result += dfs(numbers, target, cur+1, temp_sum - numbers[cur]);
    
    return result;
}


int solution(vector<int> numbers, int target) {    
    return dfs(numbers, target, 0, 0);
}