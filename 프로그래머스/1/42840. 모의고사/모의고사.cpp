#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> p1 = {1, 2, 3, 4, 5};
vector<int> p2 = {2, 1, 2, 3, 2, 4, 2, 5};
vector<int> p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> solution(vector<int> answers) {
    vector<int> scores(3, 0);
    
    for (int i=0; i < answers.size(); i++) {
        if (p1[i % p1.size()] == answers[i]) scores[0] ++;
        if (p2[i % p2.size()] == answers[i]) scores[1] ++;
        if (p3[i % p3.size()] == answers[i]) scores[2] ++;
    }
    
    int target = *max_element(scores.begin(), scores.end());
    vector<int> answer;
    
    for (int i=0; i<3; i++) {
        if (scores[i] == target) answer.push_back(i+1);
    }
    
    return answer;
}