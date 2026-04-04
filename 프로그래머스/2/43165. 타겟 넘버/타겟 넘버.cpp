#include <string>
#include <vector>

using namespace std;

int dfs(vector<int>& numbers, int& target, int idx, int current_sum) {
    if (idx == numbers.size()) {
        if (current_sum == target) return 1;
        else return 0;
    }
    
    int total = 0;
    total += dfs(numbers, target, idx + 1, current_sum + numbers[idx]);
    total += dfs(numbers, target, idx + 1, current_sum - numbers[idx]);
    return total;
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0, 0);
}