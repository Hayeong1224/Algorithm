#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    
    vector<int> arr1 = {1,2,3,4,5};
    vector<int> arr2 = {2,1,2,3,2,4,2,5};
    vector<int> arr3 = {3,3,1,1,2,2,4,4,5,5};

    vector<int> score (3, 0);

    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == arr1[i % arr1.size()]) score[0]++;
        if (answers[i] == arr2[i % arr2.size()]) score[1]++;
        if (answers[i] == arr3[i % arr3.size()]) score[2]++;
    }
    
    auto max_score = *max_element(score.begin(), score.end());
    vector<int> answer;
    
    for (int i = 0; i < score.size(); i++) {
        if (score[i] == max_score) answer.push_back(i+1);
    }
    
    return answer;
}