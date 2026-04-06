#include <string>
#include <vector>

using namespace std;

int solution(string word) {
    int weights[5] = {781, 156, 31, 6, 1};
    string vowels = "AEIOU";
    
    int ans = 0;
    for (int i = 0; i < word.size(); i++) {
        for (int j = 0; j < 5; j++) {
            if(word[i] == vowels[j]) {
                ans += j * weights[i] + 1;
                break;
            }
        }
    }
    
    return ans;
}