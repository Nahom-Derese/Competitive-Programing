#include<iostream>
#include<regex>
#include<string>
#include <algorithm>

int main(){
    std::string c;
    getline(std::cin, c);
    std::regex A("(([0-9]+)[-]([0-9]+))([;]|$)");
    std::regex B("([-0-9]+)([;]|$)");
    int sum = 0;
    for(std::sregex_iterator i = std::sregex_iterator(c.begin(), c.end(), A); i != std::sregex_iterator(); i++){
        std::smatch matches = *i;
//      std::cout << matches.str(2) << std::endl  << matches.str(3) << std::endl;
        sum += std::stoi(matches.str(3))- std::stoi(matches.str(2)) + 1;
    }
    bool flag;
    for(std::sregex_iterator i = std::sregex_iterator(c.begin(), c.end(), B); i != std::sregex_iterator(); i++){
                std::smatch matches = *i;
        flag = false;
        for(auto k : matches.str(1)){
            if(k == '-'){
                flag = true;
                break;
            }
        }
        if(!flag)
            sum++;
    }

    std::cout << sum << std::endl;

    return 0;
}


