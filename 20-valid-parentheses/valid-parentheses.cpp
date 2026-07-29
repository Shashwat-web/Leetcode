class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> mpp = {{')', '('}, {']', '['}, {'}', '{'}};

        for (char c : s) {
            if (mpp.find(c) == mpp.end()) {
                stack.push(c);
            } else if (!stack.empty() && mpp[c] == stack.top()) {
                stack.pop();
            } else {
                return false;
            }
        }

        return stack.empty();        
    }
};