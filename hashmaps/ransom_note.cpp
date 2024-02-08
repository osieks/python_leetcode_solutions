#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.length() > magazine.length()) return false;
        int arrayMagazine[26] = {0};
        for(int i=0;i<magazine.length();i++){
            arrayMagazine[magazine[i]-'a']++;
        }
        for(int x=0;x<ransomNote.length();x++){
            if(arrayMagazine[ransomNote[x]-'a'] == 0) return false;
            arrayMagazine[ransomNote[x]-'a']--;
        }
        return true;
    }
};
int main() {
    Solution sol;
    cout << sol.canConstruct("a", "b") << endl;
    cout << sol.canConstruct("aa", "ab") << endl;
    cout << sol.canConstruct("aa", "aab") << endl;
    return 0;
}