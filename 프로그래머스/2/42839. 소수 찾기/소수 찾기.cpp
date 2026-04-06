#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

bool is_prime_number(int num) {
    if (num < 2) return false;
    for (int i=2; i < int(sqrt(num))+1; i++) {
        if (num % i == 0) return false;
    }
    
    return true;
}

int solution(string numbers) {
    sort(numbers.begin(), numbers.end()); // 순열을 돌리기 위한 정렬
    
    // 모든 경우의 수
    set<int> all_nums;
    do {
        string temp = "";
        for (int i=0; i < numbers.size(); i++) {
            temp += numbers[i];
            all_nums.insert(stoi(temp));
        }
        
    } while(next_permutation(numbers.begin(), numbers.end()));
    
    // 소수 개수 세기
    int answer = 0;
    for (auto num : all_nums) {
        if (is_prime_number(num)) answer ++;
    }
    
    return answer;
}