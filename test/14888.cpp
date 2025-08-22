#include <iostream>
using namespace std;

int A[11], O[4];
int N, minSum = 1000000000, maxSum = -1000000000;

void dfs(int num, int sum) {
    // 끝나는 경우 정의
    if (num == N) {
        if (sum < minSum) minSum = sum;
        if (sum > maxSum) maxSum = sum;
        return;
    }

    // 각 단계별 할 일
    for (int i = 0; i < 4; i++) {
        if (O[i] > 0) {
            O[i]--;
            if (i == 0) dfs(num + 1, sum + A[num]);
            else if (i == 1) dfs(num + 1, sum - A[num]);
            else if (i == 2) dfs(num + 1, sum * A[num]);
            else dfs(num + 1, sum / A[num]);
            O[i]++;
        }
    }
    return;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < 4; i++) cin >> O[i];

    dfs(1, A[0]);
    cout << maxSum << '\n' << minSum;
}