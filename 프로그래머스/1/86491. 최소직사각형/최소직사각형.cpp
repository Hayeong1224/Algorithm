#include <string>
#include <vector>
#include <iostream>

using namespace std;

int max_x, max_y;
int solution(vector<vector<int>> sizes) {
    
    for(int i=0;i<sizes.size(); i++){
        if(sizes[i][0] < sizes[i][1]){
            int tmp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = tmp;
        }
    }
    
    for(int i=0; i<sizes.size(); i++){
        if(max_x < sizes[i][0]) max_x = sizes[i][0];
        if(max_y < sizes[i][1]) max_y = sizes[i][1];
    }
    
    return max_x * max_y;
}