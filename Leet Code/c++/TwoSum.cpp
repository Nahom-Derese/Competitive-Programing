#include<iostream>
#include<vector>
#include<utility>
#include<string>
#include<map>


using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> dict = {};
        for(int k=0; k < nums.size(); k++){
            int i = nums[k];
            if(dict.find(i) == dict.end()){}
            else return {dict[i], k};
            dict[target - i] = k;
        }
            return {};
    }
};
