#include <string>
#include <vector>
#include <string>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {
    return my_string.replace(s,overwrite_string.size(),overwrite_string);
}