#include<iostream>
#include<stack>
#include<vector>
#include<limits>
#include<utility>

using namespace std;

int T,M;
typedef pair<int,int> coord;

void dfs(coord start, vector<vector<char>> &adj_List, int &count);

int main(){
    cin >> T;
    char abc;
    for(int i=0;i<T; i++){
        cin >> M;
        vector<vector<char>> In(M);
        for(int k=0;k<M; k++){ for(int l=0;l<M; l++){ 
            cin >> abc;
            In[k].push_back(abc);
            }}
        int count = 0;
        for(int k=0;k<M; k++){
            for(int l=0;l<M; l++){
                coord start(k,l);
                if(In[k][l] == 'x') dfs(start, In , count);
            }
        }
        cout << "Case " << i+1 << ": " << count << endl;
    }    
    return 0;
}

void dfs(coord start, vector<vector<char>> &adj_List, int &count){
    count++;
    stack<coord> dfsu;
    dfsu.push(start);
    while(!dfsu.empty()){
        coord temp = dfsu.top();
        dfsu.pop();
        adj_List[temp.first][temp.second] = 'y';
        
        if(temp.first < M-1) {
            coord d(temp.first + 1, temp.second);
            if(adj_List[temp.first + 1][temp.second] == 'x'|| adj_List[temp.first + 1][temp.second] == '@') dfsu.push(d);
        }
        
        if(temp.second < M-1) {
            coord d(temp.first, temp.second + 1);
            if(adj_List[temp.first][temp.second + 1] == 'x'|| adj_List[temp.first][temp.second + 1] == '@') dfsu.push(d);
        }
}
}