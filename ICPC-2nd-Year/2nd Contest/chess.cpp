#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <map>
#include <queue>
#include <cmath>

using namespace std;


// Global Var's
int count = 0;
int row, col;


// TYPEDEFS
typedef pair<int, int> coord;
typedef vector<vector<char>> table;
typedef map<int, vector<coord>> adj_list;
typedef vector<coord> single_adj_list;


// Functions Declarations
single_adj_list Adj_Generator(table &chess, coord &which);
single_adj_list Knight_Moves(table &chess, coord &which);
void bfs(table &chess, coord &start);
void fill(table &chess, coord &start);


// Main
int main()
{
    ios_base::sync_with_stdio( false );
    cin.tie(0);
    cout.tie(0);
    while (cin >> row >> col)
    {
        count = 0;
        int ans;
        if (row == 0 && col == 0)
            break;
        else if (row == 0 || col == 0)
        {
            cout << 0 << " knights may be placed on a " << row << " row " << col << " column board." << endl;
            continue;
        }
        else if(row==1) ans = col;
        else if(col==1) ans = row;
        ans = floor(((row*col)/2.0)+1);
        cout << ans << " knights may be placed on a " << row << " row " << col << " column board." << endl;
        
        // else{
        //     table chess(row, vector<char>(col, '0'));
        //     coord starter = {0,0};
        //     bfs(chess, starter);
        //     cout << count << " knights may be placed on a " << row << " row " << col << " column board." << endl;
        // }
        
    }
    return 0;
}

// Functions
single_adj_list Adj_Generator(table &chess, coord &which)
{
    single_adj_list response;
    vector<coord> drn = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1},
        {1,1},
        {-1, -1},
        {1,-1},
        {-1,1}};

        for (int k = 0; k < 4; k++)
        {
            if (which.second + drn[k].second >= 0 && which.first + drn[k].first >= 0 && which.second + drn[k].second < col && which.first + drn[k].first < row)
                response.push_back({which.first + drn[k].first, which.second + drn[k].second});
        }
    return response;
}

single_adj_list Knight_Moves(table &chess, coord &which)
{
    single_adj_list response;
    vector<coord> drn = {
        {1, 2},
        {1, -2},
        {-1, 2},
        {-1, -2},

        {2, 1},
        {2, -1},
        {-2, 1},
        {-2, -1}};
        for (auto d : drn)
            if (which.first+ d.first >= 0 && which.first+ d.first < row && which.second+ d.second >= 0 && which.second+ d.second < col)
                response.push_back({which.first+ d.first, which.second+ d.second});
    return response;
}

void bfs(table &chess, coord &start)
{
    queue<coord> Q;
    Q.push(start);
    while (!Q.empty())
    {
        coord temp = Q.front();
        Q.pop();
        fill(chess, temp);
        coord which = {temp.first, temp.second};
        for (auto i: Adj_Generator(chess, which))
            if (chess[i.first][i.second] == '0')
                Q.push(i);
    }
}

void fill(table &chess, coord &start)
{
    queue<vector<int>> Q;
    if (chess[start.first][start.second] == '0')
    {
        vector<int> V = {start.first, start.second, 0};
        Q.push(V);
    };
    while (!Q.empty())
    {
        vector<int> temp = {Q.front()[0], Q.front()[1], Q.front()[2]};
        Q.pop();
        if (chess[temp[0]][temp[1]] == 'X' or chess[temp[0]][temp[1]] == 'N')
            continue;

        chess[temp[0]][temp[1]] = temp[2] == 1 ? 'X' : 'N';
        if (temp[2] == 0)
            count++;
        int sym = temp[2] == 1 ? 0 : 1;
        coord which = {temp[0], temp[1]};
        for (auto i: Knight_Moves(chess, which))
            if (chess[i.first][i.second] == '0')
                Q.push({i.first, i.second, sym});
    }
}
