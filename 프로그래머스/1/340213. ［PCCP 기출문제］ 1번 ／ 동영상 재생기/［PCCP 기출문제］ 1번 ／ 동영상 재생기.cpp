#include <string>
#include <vector>

using namespace std;

string solution(string video_len, string pos, string op_start, string op_end, vector<string> commands) {
    string answer = "";
    int totalLen = stoi(video_len.substr(0,2)) * 60 + stoi(video_len.substr(3,2));
    int totalPos = stoi(pos.substr(0,2)) * 60 + stoi(pos.substr(3,2));
    int totalOpStart = stoi(op_start.substr(0,2)) * 60 + stoi(op_start.substr(3,2));
    int totalOpEnd = stoi(op_end.substr(0,2)) * 60 + stoi(op_end.substr(3,2));
    
    for(int i=0; i<commands.size(); i++){
        if(totalOpStart <= totalPos && totalPos <= totalOpEnd) totalPos = totalOpEnd;
        if(commands[i].compare("prev") == 0) totalPos = max(totalPos-10, 0);
        else totalPos = min(totalPos+10, totalLen);
    }
    
    if(totalOpStart <= totalPos && totalPos <= totalOpEnd) totalPos = totalOpEnd;
    
    int pos_min = totalPos / 60;
    int pos_sec = totalPos % 60;
    
    string min = to_string(pos_min);
    string sec = to_string(pos_sec);
    
    if(min.size() < 2) min = '0' + min;
    if(sec.size() < 2) sec = '0' + sec;
    
    answer = min + ':' + sec;
    
    return answer;
}