#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string str;
    cin >> str;
    stack<char> s;
    int temp=1, result = 0;
    char pre;
    for(int i=0; i<str.length();i++){
        if(str[i] == ')') {
            if(!s.empty() && s.top() == '(') {
                if(pre == '(') result += temp;
                temp /= 2;
                s.pop();
            }
            else {
                result = 0;
                break;
            }
        }
        else if (str[i] == ']'){
            if (!s.empty() && s.top() == '[') {
                if (pre == '[') result += temp;
                temp /= 3;
                s.pop();
            }
            else {
                result = 0;
                break;
            }
        }
        else if (str[i] == '(') {
            temp *= 2;
            s.push(str[i]);
        }
        else if (str[i] == '[') {
            temp *= 3;
            s.push(str[i]);
        }
        pre = str[i];
    }
    if(!s.empty()) result=0;
    cout << result;  
}