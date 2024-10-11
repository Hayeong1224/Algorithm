#include <bits/stdc++.h>

using namespace std;

bool comparePlays(pair<int,int> &a, pair<int,int> &b){ //고유번호, 재생수
    if(a.second == b.second) return a.first < b.first; //고유번호 오름차순
    else return a.second > b.second; //재생 수 내림차순
}
bool compareGenres(pair<string,int> &a, pair<string,int> &b){//장르, 총 재생수
    return a.second > b.second; //총 재생 수 내림차순
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> totalPlays; //장르별 총 재생수
    unordered_map<string, vector<pair<int,int>>> genrePlays; //곡별 재생 수
    
    for(int i=0;i<genres.size();i++){
        totalPlays[genres[i]] += plays[i];
        genrePlays[genres[i]].push_back(make_pair(i,plays[i]));
    }
    
    vector<pair<string, int>> total(totalPlays.begin(), totalPlays.end());
    sort(total.begin(), total.end(), compareGenres);
    
    for(const auto& t : total){
        string genre = t.first;
        sort(genrePlays[genre].begin(), genrePlays[genre].end(),comparePlays);
    }
    
    for(const auto& t : total){
        string genre = t.first;
        if(genrePlays[genre].size() > 1) for(int i=0; i<2; i++) answer.push_back(genrePlays[genre][i].first);
        else answer.push_back(genrePlays[genre][0].first);
    }
    
    return answer;
}