#include<iostream>
#include<regex>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        if (regex_match (s, regex(p))){
            return true;
        }
        return false;
    }
};

int main(){
    cout << Solution().isMatch("aa", ".*") << endl;
    return 0;
}