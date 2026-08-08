class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp ;
        vector<int> ans ;
        int n = nums.size() ;
        for(auto x : nums)
            mp[x] ++ ;

        vector<pair<int,int>> freq ;

        for(auto x : mp){
            freq.push_back({x.second, x.first}) ;
        }

        sort(freq.rbegin(), freq.rend()) ;

        for(int i = 0 ; i < k ; i ++)
            ans.push_back(freq[i].second) ;
        return ans ;
    }
};
