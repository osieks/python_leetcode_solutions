package hashmaps.ransom_note_in_java;

public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) return false;
        int[] arrayMagazine = new int[26];
        for(int i = 0; i < magazine.length(); i++){
            arrayMagazine[magazine.charAt(i) - 'a']++;
        }
        for(int x = 0; x < ransomNote.length(); x++){
            if(arrayMagazine[ransomNote.charAt(x) - 'a'] == 0) return false;
            arrayMagazine[ransomNote.charAt(x) - 'a']--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.canConstruct("a", "b"));
        System.out.println(sol.canConstruct("aa", "ab"));
        System.out.println(sol.canConstruct("aa", "aab"));
    }
}
