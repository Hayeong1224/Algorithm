#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    
    // t시간 동안 심사관들이 총 몇 명을 심사할 수 있는지! n보다 크면서 가장 작은 t 구하기 -> t를 정하는 이분 탐색 진행
    sort(times.begin(), times.end());
    
    long long low = 1;
    long long high = (long long)times.back() * n;
    
    while (low <= high) {
        long long mid = (low + high) / 2;
        long long total = 0;
        
        for (auto t : times) {
            total += (mid / t);
            if (total >= n) break;
        }
        
        if (total >= n) {
            answer = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    return answer;
}