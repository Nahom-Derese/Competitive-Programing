#include<iostream>
#include<string>
#include<utility>
#include<vector>
#include<queue>


using namespace std;

pair<int,int> maxi;
void bfs(vector<vector<char>> &Adj_List, pair<int,int> start);

int main(){
    vector<pair<int,int>> starts;
    cin >> maxi.first >> maxi.second;
    vector<vector<char>> graph(maxi.first);
    char single;
    for(int i = 0; i < maxi.first; i++){ 
        for(int j = 0; j < maxi.second; j++){ 
            cin >> single;
            graph[i].push_back(single);
            if(graph[i][j] == 'V') starts.push_back({i, j});
        }}

    for(auto k:starts) bfs(graph, k);

    for(int i = 0; i < maxi.first; i++){ 
        for(int j = 0; j < maxi.second; j++) cout << graph[i][j];
        cout << endl;
    }
    return 0;
}

void bfs(vector<vector<char>> &graph, pair<int,int> start){
    queue<pair<int,int>> q;
    q.push({start.first, start.second});
    
    while(!q.empty()){
        pair<int,int> temp = q.front();
        q.pop();
        graph[temp.first][temp.second] = 'V';
        if(temp.first != maxi.first-1) if(graph[temp.first+1][temp.second] != '#') q.push({temp.first+1,temp.second});
        else{ 
            if(temp.second != maxi.second-1 && graph[temp.first][temp.second+1] != '#' && graph[temp.first][temp.second+1] != 'V') 
                q.push({temp.first,temp.second+1});
            if(temp.second != 0 && graph[temp.first][temp.second-1] != '#' && graph[temp.first][temp.second-1] != 'V') 
                q.push({temp.first,temp.second-1});
        }
        }
}
