class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        if (s.size()==0) return true;
        if (s[0] == '(' or s[0] == '[' or s[0]== '{') st.push(s[0]);
        else return false;
        for (int i = 1 ; i < s.size() ; i++ ){
            if (s[i] == '(' or s[i] == '[' or s[i]== '{' or st.empty()) st.push(s[i]);
            else if (s[i] == ')' && st.top() == '(') st.pop();
            else if (s[i] == '}' && st.top() == '{') st.pop();
            else if (s[i] == ']' && st.top() == '[') st.pop();
            else return false;
        }
        if (!st.empty()) return false;
        return true;
    }
};