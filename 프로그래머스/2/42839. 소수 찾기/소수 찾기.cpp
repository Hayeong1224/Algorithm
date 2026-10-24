#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;

// 소수 판별
bool is_prime(int val) {
    if (val < 2) return false;
    for (int i = 2; i <= sqrt(val); i++) {
        if (val % i == 0) return false;
    }
    return true;
}

int solution(string numbers) {
    // 순열 만들기 위해 정렬
    sort(numbers.begin(), numbers.end());
    
    set<int> all_nums;
    do {
        string temp = "";
        for(int i=0; i<numbers.size(); i++) {
            temp += numbers[i];
            all_nums.insert(stoi(temp));
        }
    } while (next_permutation(numbers.begin(), numbers.end()));
    
    int cnt = 0;
    for (const auto& num: all_nums) {
        if(is_prime(num)) cnt++;
    }
    
    return cnt;
}