// 문제) 배열 정렬  n^2도 가능하다면 버블 정렬 가능! -> 버블 정렬 구현해보기

//직접 작성한 코드

#include <vector>
#include <algorithm>


using namespace std;

vector<int> solution(vector<int> arr) {
    for(size_t i = 0; i < arr.size() -1 ; i++){
        for(size_t j = 0; j < arr.size() - i -1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
    return arr;
 }


//아래 코드는 테스트 코드 입니다.
#include <iterator>
#include <iostream>

void print(vector<int> vec) {
    copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " "));
    cout << endl;
}

int main() {
    print(solution({1, -5, 2, 4, 3}));      // -5 1 2 3 4 
    print(solution({2, 1, 1, 3, 2, 5, 4})); // 1 1 2 2 3 4 5 
    print(solution({6, 1, 7}));             // 1 6 7 
    
    return 0;
}