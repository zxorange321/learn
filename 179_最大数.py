#!/usr/bin/python	


'''
最大数

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

'''

#cpp not by myself
'''
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> numStr;
        for(int num: nums)
            numStr.push_back(to_string(num));
        sort(numStr.begin(), numStr.end(), cmp);
        if(numStr.size() && numStr[0] == "0") return "0";
        string s = "";
        for(string num: numStr)
            s += num;
        return s;
    }
    static bool cmp(string i, string j){
        return i + j > j + i;
    }
};

'''