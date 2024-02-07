#include <iostream>
#include <string>

using namespace std;

class Solution {
    /*  0ms 7.5mb
        beats:
            100% in runtime
            25.75% in memory
    */ 
    
public:
    bool isSubsequence(string s, string t) {
        if(s.length() == 0)
            return true;
        else if(t.length() == 0)
            return false;
        int y = 0;
        for(int x = 0; x < t.length(); x++) {
            cout << t[x] << " " << s[y] << endl;
            if(t[x] == s[y]) {
                y++;
                if(y >= s.length())
                    return true;
            }
        }
        return false;
    }
};

int main() {
    Solution sol;
    cout << sol.isSubsequence("abc", "ahbgdc") << endl;
    cout << sol.isSubsequence("axc", "ahbgdc") << endl;
    cout << sol.isSubsequence("", "ahbgdc") << endl;
    return 0;
}