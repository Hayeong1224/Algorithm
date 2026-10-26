#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>

using namespace std;

vector<string> solution(vector<string> record) {
    unordered_map<string, string> id_name;
    
    // 최신 버전 닉네임으로 업데이트
    for (const auto& com : record) {
        // 문자열 자르기
        stringstream ss(com);
        string command, uid, nickname;
        ss >> command >> uid;
        
        if (command == "Enter" || command == "Change") {
            ss >> nickname;
            id_name[uid] = nickname;
        }
    }
    
    vector<string> answer;

    for (const auto& com : record) {
        stringstream ss(com);
        string command, uid, nickname;
        
        ss >> command >> uid;
        nickname = id_name[uid];
        
        if (command == "Enter") {
            answer.push_back(nickname+"님이 들어왔습니다.");
        }
        else if (command == "Leave") {
            answer.push_back(nickname+"님이 나갔습니다.");
        }
    }
    
    return answer;
}