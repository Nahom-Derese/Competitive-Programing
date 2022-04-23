#include<iostream>
#include<stack>
#include<vector>
#include <limits>
using namespace std;

int N,H,L;
void dfs(int start,int length, vector<vector<int>>adj_List, vector<int> &HI);

int main(){
    int a = std::numeric_limits<int>::max();
    cin >> N >> H >> L;
    int Horror[H] = {0};
    int max=0, maxI=0;
    vector<int> HI(N, a);
    int Edge_List[L][2] = {{0,0}};
    vector<vector<int>> adj_List(N); 
    for(int i=0; i < H; i++){
        cin >> Horror[i];
        HI[Horror[i]] = 0;
    }    
    for(int j=0; j < L; j++) cin >> Edge_List[j][0] >>  Edge_List[j][1];
    for(int j=0; j < L; j++) {
        adj_List[Edge_List[j][0]].push_back(Edge_List[j][1]);
        adj_List[Edge_List[j][1]].push_back(Edge_List[j][0]);
    }
    for(int i=0; i < H; i++) dfs(Horror[i],N, adj_List, HI);
    for(int j=0; j < N; j++) if(HI[j] != a && HI[j] != 0) HI[j]-=a;
    for(int j=0; j < N; j++) {
        if(HI[j] > max) { 
            max = HI[j];
            maxI = j;
        }
    }
    cout << maxI << endl;
    return 0;
}

void dfs(int start, int length, vector<vector<int>>adj_List, vector<int> &HI){
    bool Visited[length] = {false};
    stack<int> dfs;
    dfs.push(start);
    while(!dfs.empty()){
        int temp = dfs.top();
        if(HI[temp]!=0 && !Visited[temp]) HI[temp]+=1;
        Visited[temp] = true;
        dfs.pop();
        for(auto i:adj_List[temp]){
            if(!Visited[i]) dfs.push(i);
        }
}}