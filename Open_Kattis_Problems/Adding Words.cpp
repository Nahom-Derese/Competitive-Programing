#include <iostream>
#include <regex>
#include <utility>

int main() {
    // Write C++ code here
    std::string a,b,e;
    std::map<std::string,int> c;
    while(std::cin >> a){
        if(a == "def"){
            int d;
            std::cin >> b >> d;
            c[b] = d;
        }
        else if(a == "calc"){
            bool flag2 = false,flag  = false;
            std::string e;
            std::vector<int> nums;
            std::cin.clear();
            getline(std::cin, e);
            std::regex J("[a-z]+");
            std::regex L("[+-]");
            auto words_begin = std::sregex_iterator(e.begin(),e.end(),J);
            auto words_end = std::sregex_iterator();
            auto opp_begin = std::sregex_iterator(e.begin(),e.end(),L);
            auto opp_end = std::sregex_iterator();
            for (std::sregex_iterator i = words_begin; i != words_end; i++)
            {
                std::smatch match = *i;
                std::string match_str = match.str();
                char *v = &e[1];
                if(c.count(match_str)!=0)
                    nums.push_back(c[match_str]);
                else{
                    flag = true;
                    std::cout << v << " unknown" << '\n';
                    break;
                }
            }
            for (std::sregex_iterator i = opp_begin; i != opp_end; i++)
            {
                if (flag)
                    break;
                
                std::smatch match = *i;
                std::string match_str = match.str();
                if (match_str == "+")
                {
                    nums[1] = nums[0] + nums[1];
                    nums.erase(nums.begin());
                }
                if (match_str == "-")
                {
                    nums[1] = nums[0] - nums[1];
                    nums.erase(nums.begin());
                }
            }
    char *v = &e[1];
            for (auto i:c)
            {
                if (flag)
                    break;
                std::string q = i.first;
                char *y = &q[0];
                if (nums[0] == i.second){
                    printf("%s %s\n", v, y);
                    flag2 = true;
                }
            }
            if(!flag2 && !flag)
                std::cout << v << " unknown" << '\n';
        }
        else if(a == "clear"){
            c.clear();
            continue;
        }
    }
    
    return 0;
}