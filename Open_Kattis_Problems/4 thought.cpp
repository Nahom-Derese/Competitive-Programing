#include <bits/stdc++.h>
using namespace std;

char signs[4] = {'*', '/', '-', '+'};

int calculator(char a, char b, char c)
{
    vector<int> t = {4, 4, 4, 4};
    vector<char> o = {a, b, c};
    vector<char> y = {a, b, c};
    bool w = true;
    for (short i = 1; i < 3; i++)
    {
        bool x = y[i - 1] != '*' ? true : false;
        x = y[i - 1] != '/' && x ? true : false;
        if ((y[i] == '*' || y[i] == '/') && x)
        {
            if (y[i] == '*' && w)
            {
                y[i] = y[i - 1];
                y[i - 1] = '*';
                if (i == 2 && w)
                {
                    i -= 2;
                    w = false;
                }
            }
            if (y[i] == '/' && w)
            {
                y[i] = y[i - 1];
                y[i - 1] = '/';
                if (i == 2 && w)
                {
                    i -= 2;
                    w = false;
                }
            }
        }
    }

    int counter = 0;
    while (t.size() != 1)
    {
        bool s = true;

        if (y.size() != 0 && y[0] == '*')
        {
            if (y[0] == o[counter] || y[0] == o[counter - 1])
            {
                t[1] = t[0] * t[1];
                t.erase(t.begin());
                y.erase(y.begin());
                o[counter] = '0';
            }
            else if (y[0] == o[1 + counter])
            {
                t[2] = t[1] * t[2];
                t.erase(t.begin() + 1);
                y.erase(y.begin());
                o[counter + 1] = '0';
            }
            else
            {
                t[t.size() - 2] = t[t.size() - 2] * t[t.size() - 1];
                t.pop_back();
                o[counter] = '0';
            }
            s = false;
            counter++;
        }

        else if (y.size() != 0 && y[0] == '/')
        {
            if (y[0] == o[counter] || y[0] == o[counter - 1])
            {
                t[1] = t[0] / t[1];
                t.erase(t.begin());
                y.erase(y.begin());
                o[counter] = '0';
            }
            else if (y[0] == o[1 + counter])
            {
                t[2] = t[1] / t[2];
                t.erase(t.begin() + 1);
                y.erase(y.begin());
                o[counter + 1] = '0';
            }
            else
            {
                t[t.size() - 2] = t[t.size() - 2] / t[t.size() - 1];
                t.pop_back();
                o[counter] = '0';
            }
            s = false;
            counter++;
        }

        else if (y.size() != 0 && y[0] == '-')
        {
            if (y[0] == o[counter] || y[0] == o[counter - 1])
            {
                t[1] = t[0] - t[1];
                t.erase(t.begin());
                y.erase(y.begin());
                o[counter] = '0';
            }
            else if (y[0] == o[1 + counter])
            {
                t[2] = t[1] - t[2];
                t.erase(t.begin() + 1);
                y.erase(y.begin());
                o[counter + 1] = '0';
            }
            else
            {
                t[t.size() - 2] = t[t.size() - 2] - t[t.size() - 1];
                t.pop_back();
                o[counter] = '0';
            }
            s = false;
            counter++;
        }

        else if (y.size() != 0 && y[0] == '+')
        {
            if (y[0] == o[counter] || y[0] == o[counter - 1])
            {
                t[1] = t[0] + t[1];
                t.erase(t.begin());
                y.erase(y.begin());
                o[counter] = '0';
            }
            else if (y[0] == o[1 + counter])
            {
                t[2] = t[1] + t[2];
                t.erase(t.begin() + 1);
                y.erase(y.begin());
                o[counter + 1] = '0';
            }
            else
            {
                t[t.size() - 2] = t[t.size() - 2] + t[t.size() - 1];
                t.pop_back();
                o[counter] = '0';
            }
            s = false;
            counter++;
        }
    }

    return t[0];
}

int main()
{
    int n;
    cin >> n;
    for (short i = 0; i < n; i++)
    {
        int t,counter = 0;
        cin >> t;
        for (short p = 0; p < 4; p++)
        {
            for (short j = 0; j < 4; j++)
            {
                for (short k = 0; k < 4; k++)
                {
                    if (calculator(signs[p], signs[j], signs[k]) == t && counter == 0){
                        cout << "4 " << signs[p] << " 4 " << signs[j] << " 4 " << signs[k] << " 4 "
                         << "= " << calculator(signs[p], signs[j], signs[k]) << endl;
                         counter++;
                    }
                    else if(p==3 && j ==3 && k==3 && counter == 0)
                        cout << "no solution" << endl;
                }
            }
        }
    }

    return 0;
}
