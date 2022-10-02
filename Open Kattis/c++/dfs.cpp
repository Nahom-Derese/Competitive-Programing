#include<bits/stdc++.h>
#define LOG(s) std::cout << s << std::endl;


void dfs(std::map<std::string, bool> &visited, std::map<std::string,  std::vector<std::string>> neighbours, std::string st){
    if(!visited[st]){
        LOG(st)
        visited[st] = true;
        for (auto i : neighbours[st])
            dfs(visited, neighbours, i);
    }
}

int main(){
    std::map<std::string, bool> visited;
    std::map<std::string, std::vector<std::string>> neighbours = {
        {"a", {"b", "d"}},
        {"d", {"a"}},
        {"c", {"e", "f", "g"}},
        {"b", {"a", "c"}},
        {"e", {"f", "c"}},
        {"f", {"e", "c"}}
    };

    dfs(visited, neighbours, "a");


    return 0;
}