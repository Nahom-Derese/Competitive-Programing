#include <bits/stdc++.h>
using namespace std;

bool check(vector<int> y, short o)
{
    switch (o)
    {
    case 0:
        for (short j = 0; j < 4; j++)
    {
        if (j < 3 && y[j] == 0 && y[j + 1] != 0)
            return true;
    }
        break;
    case 1:
        for (short j = 0; j < 4; j++)
    {
        if (j < 3 && y[j] == 0 && y[j + 1] != 0)
            return true;
    }
        break;
    case 2:
        for (short j = 0; j < 4; j++)
    {
        if (j > 0 && y[j] == 0 && y[j - 1] != 0)
            return true;
    }
        break;
    case 3:
        for (short j = 0; j < 4; j++)
    {
        if (j > 0 && y[j] == 0 && y[j - 1] != 0)
            return true;
    }
        break;
    default:
        return false;
    }
    return false;
}

vector<int> reOrder(vector<int> y, short o){
    short r = 0;
        switch (o){
        case 0:
            while(check(y,o) && r<4){
        if (r > 1 && y[r - 1] == 0 && y[r - 2] == 0)
        {
            y[r - 2] = y[r];
            y[r] = 0;
        }
        if (r != 0 && y[r - 1] == 0)
        {
            y[r - 1] = y[r];
            y[r] = 0;
        }
            r++;
    }
            break;
        case 1:
            while(check(y,o) && r<4){
        if (r > 1 && y[r-1] == 0 && y[r-2] == 0)
            {
                y[r-2] = y[r];
                y[r] = 0;
            }
        if (r != 0 && y[r-1] == 0 && y[r] != 0)
            {
                y[r-1] = y[r];
                y[r] = 0;
            }
            r++;
            }
            break;
        case 2:
            while(check(y,o) && r<4){
        if (r < 2 && y[r + 1] == 0 && y[r + 2] == 0)
        {
            y[r + 2] = y[r];
            y[r] = 0;
        }
        if (r != 3 && y[r + 1] == 0)
        {
            y[r + 1] = y[r];
            y[r] = 0;
        }
            r++;
            }
            break;
        case 3:
        r = 3;
            while(check(y,o) && r>-1){
        if ( r<2 && y[r+1] == 0 && y[r+2] == 0)
        {
            y[r+2] = y[r];
            y[r] = 0;
        }
        if ( r != 3 && y[r+1] == 0 && y[r] != 0)
        {
            y[r+1] = y[r];
            y[r] = 0;
        }
            r--;
            }
            break;
        default:
            break;
        }
        return y;
    }

int main()
{
    // Declaring inputs(string) and Table(vector)
    string inputs[4], T;
    vector<vector<int>> Table(4, vector<int>(4, 0));

    // Get table input from the keyboard
    for (short i = 0; i < 4; i++)
    {
        getline(cin, inputs[i]);
        stringstream X(inputs[i]);
        short j = 0;
        while (getline(X, T, ' '))
        {
            Table[i][j] = stoi(T);
            j++;
        }
    }

    // Get touch input from keyboard
    short x;
    cin >> x;

     vector<vector<int>> column = Table;

     for (short i = 0; i < 4; i++)
     {
         for (short j = 0; j < 4; j++)
         {
             column[i][j] = Table[j][i];
         }
     }
     
    // Logic going on here to put the Output
    switch (x)
    {
    case 0:
        for (short i = 0; i < 4; i++)
        {
            int m = 0;
            int u = 0;
            for (short j = 0; j < 4; j++)
            {
                if(j>0 && m == 1 && u < j-1)
                    m = 0;
                Table[i] = reOrder(Table[i],x);
                if (j < 3 && Table[i][j] == Table[i][j + 1])
                {
                    Table[i][j] *= 2;
                    Table[i][j + 1] = 0;
                    m++;
                    u = j;
                }
                else if (j < 2)
                {
                    if (Table[i][j] == Table[i][j + 2] && Table[i][j + 1] == 0)
                    {
                        Table[i][j] *= 2;
                        Table[i][j + 2] = 0;
                    }
                }
                else if (Table[i][0] == Table[i][3] && Table[i][1] == 0 && Table[i][2] == 0)
                {
                    Table[i][0] *= 2;
                    Table[i][3] = 0;
                }
                Table[i] = reOrder(Table[i],x);            }
        }
        break;
    case 1:
        for (short i = 0; i < 4; i++)
        {
            int m = 0;
            int u = 0;
            for (short j = 0; j < 4; j++)
            {
                if(j>0 && m == 1 && u < j-1)
                    m = 0;
                column[i] = reOrder(column[i],x);
                if (j < 3 && column[i][j] == column[i][j+1])
                    {
                        column[i][j] *= 2;
                        column[i][j+1] = 0;
                        m++;
                        u = j;
                    }
                else if (j < 2 && i < 2)
                {
                    if (column[i][j] == column[i][j+2] && column[i][j+1] == 0)
                    {
                        column[i][j] *= 2;
                        column[i][j+2] = 0;
                    }
                }
                else if (column[i][0] == column[i][3] && column[i][1] == 0 && column[i][2] == 0)
                {
                    column[i][0] *= 2;
                    column[i][3] = 0;
                }
                column[i] = reOrder(column[i],x);
            }
        }
        break;
    case 2:
        for (short i = 0; i < 4; i++)
        {
            int m = 0;
            int u = 0;
            for (short j = 3; j > -1; j--)
            {
                Table[i] = reOrder(Table[i],x);
                if(j>0 && m == 1 && u > j-1)
                    m = 0;
                if (j > 0 && Table[i][j] == Table[i][j - 1] && m == 0)
                    {
                        Table[i][j] *= 2;
                        Table[i][j-1] = 0;
                        m++;
                        u = j;
                    }
                else if (j > 2 && Table[i][j] == Table[i][j - 2] && Table[i][j - 1] == 0)
                    {
                        Table[i][j] *= 2;
                        Table[i][j-2] = 0;
                    }
                else if (Table[i][0] == Table[i][3] && Table[i][1] == 0 && Table[i][2] == 0)
                {
                    Table[i][3] *= 2;
                    Table[i][0] = 0;
                }
                Table[i] = reOrder(Table[i],x);
            }
        }
        break;
    case 3:
        for (short i = 0; i < 4; i++)
        {
            int m = 0;
            int u = 0;
            for (short j = 3; j > -1; j--)
            {
                column[i] = reOrder(column[i],x);
                if(j>0 && m == 1 && u > j-1)
                    m = 0;
                if (j > 0 && column[i][j] == column[i][j - 1] && m == 0)
                    {
                        column[i][j] *= 2;
                        column[i][j-1] = 0;
                        m++;
                        u = j;
                    }
                else if (j > 1 && column[i][j] == column[i][j - 2] && column[i][j - 1] == 0)
                    {
                        column[i][j] *= 2;
                        column[i][j - 2] = 0;
                    }
                else if (column[i][0] == column[i][3] && column[i][1] == 0 && column[i][2] == 0)
                {
                    column[i][3] *= 2;
                    column[i][0] = 0;
                }
                column[i] = reOrder(column[i],x);            }
        }
        break;

    default:
        cout << "Please a no 0 - 3" << endl;
        break;
    }

    // Display The move
    for (short i = 0; i < 4; i++)
    {
        for (short j = 0; j < 4; j++){
            if (x == 1 || x == 3)
                cout << column[j][i] << ' ';
            else
                cout << Table[i][j] << ' ';
        }
        cout << endl;
    }

    // Halt the program after process done
    return 0;
}
