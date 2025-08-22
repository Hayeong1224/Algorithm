// 문제) 배열 제어 - 중복값 제거, 내림차순 정렬
// 접근) n <= 1000-> n^2도 가능
//      중복값 제거 - unique(), 내림차순 정렬 - sort()

//직접 작성한 코드
#include<vector>
#include<algorithm>

using namespace std;

bool compare(int a, int b) {
    return a>b;
}

vector<int> solution(vector<int> lst) {
    //sort(lst.begin(), lst.end(), compare);//내림차순 정렬 - 방법 1
    //sort(lst.begin(), lst.end(), greater<int>());//내림차순 정렬 - 방법 2
    sort(lst.rbegin(), lst.rend()); //내림차순 정렬 - 방법 3
    lst.erase(unique(lst.begin(), lst.end()), lst.end()); //중복값 제거
    return lst;
}



//아래 코드는 테스트 코드 입니다.
#include <iostream>
#include <iterator>
void print(vector<int> vec)
{
    copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " "));
    cout << endl;
}

int main()
{
    print(solution({4, 2, 2, 1, 1, 3, 4})); // 4 3 2 1  
    print(solution({2, 1, 1, 3, 2, 5, 4})); // 5 4 3 2 1
    
    return 0;
}