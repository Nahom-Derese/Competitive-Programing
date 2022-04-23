#include<bits/stdc++.h>
using namespace std;

int main(){
    string direction;
    int start;
    vector<char> g;
    getline(cin, direction);
    cin >> start;
    map<int, pair<int, int>> w = {
        {1 , {2,0}},
        {2 , {2,1}},
        {3 , {2,2}},
        {4 , {1,0}},
        {5 , {1,1}},
        {6 , {1,2}},
        {7 , {0,0}},
        {8 , {0,1}},
        {9 , {0,1}},
    };
    int ww[3][3] = {{7 ,8 ,9},{4 ,5 ,6 },{1 ,2 ,3}};
    int count = 0;

    for(int i = 0; i < direction.size(); i++){
        if(direction[i] == 'R'){count++;}
        else{
            for(int i = 0; i < count%3; i++) g.push_back('R');
            count = 0;
        }
        if(direction[i] == 'U'){count++;}
        else {
            for(int i = 0; i < count%3; i++) g.push_back('U');
            count = 0;
        }
        if(direction[i] == 'L'){count++;}
        else {
            for(int i = 0; i < count%3; i++) g.push_back('L');
            count = 0;
        }
        if(direction[i] == 'D'){count++;}
        else {
            for(int i = 0; i < count%3; i++) g.push_back('D');
            count = 0;
        }
    }
    int current = start;
    
    for(auto j:g){
        if(j == 'R') {
            if(w[current].second < 2) current = ww[w[current].first][w[current].second+1];
            else current = ww[w[current].first][w[current].second-2];
        }
        if(j == 'L') {
            if(w[current].second > 0) current = ww[w[current].first][w[current].second-1];
            else current = ww[w[current].first][w[current].second+2];
        }
        if(j == 'D') {
            if(w[current].first < 2) current = ww[w[current].first+1][w[current].second];
            else current = ww[w[current].first-2][w[current].second];
        }
        if(j == 'U') {
            if(w[current].second > 0) current = ww[w[current].first-1][w[current].second];
            else current = ww[w[current].first+2][w[current].second];
        }
    }
    
    cout << current << endl;

    return 0;
}