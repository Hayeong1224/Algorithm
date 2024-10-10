#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int n = progresses.size();
    vector<int> days_left(n);

    //배포 예상일 7, 3, 9
    for(int i=0; i < n; i++) days_left[i] = ceil((100.0-progresses[i])/speeds[i]);
    
    int count = 0;
    int max_day = days_left[0];
    
    for(int i=0; i<n; i++){
        if(days_left[i] <= max_day) count ++;
        else{
            answer.push_back(count);
            max_day = days_left[i];
            count = 1;
        }
    }
    
    answer.push_back(count);
    return answer;
}