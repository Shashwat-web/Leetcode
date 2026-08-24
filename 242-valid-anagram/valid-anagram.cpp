class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false ;

        unordered_map<char,int> mp1 ;
        unordered_map<char,int> mp2 ;

        for(auto x : s)
            mp1[x]++ ;

        for(auto x : t)
            mp2[x]++ ;

        return mp1 == mp2 ;
    }
};