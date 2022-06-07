#include<iostream>
#include<vector>
#include<unordered_set>
#include<utility>
#include<string>
#include<stack>
#include<map>

using namespace std;


struct Node
{
    string name;
    Node* next;
};

Node* head = NULL;
Node* tail = NULL;

void split(string s, string del, map<string, unordered_set<string>> &u){
    int start = 0;
    int end = s.find(del);
    string first;
    unordered_set<string> r;
    while (end != -1) {
        if (start == 0) first = s.substr(start, end - start);
        else{
            r.insert(s.substr(start, end - start));
            u[s.substr(start, end - start)].insert(first);
        }
        start = end + del.size();
        end = s.find(del, start);
    }
    r.insert((s.substr(start, end - start)));
    u[s.substr(start, end - start)].insert(first);
    u[first] = r;
}

void dfs(map<string,unordered_set<string>> Adj, string start, string end){
    stack<string> q,branches;
    q.push(start);
    vector<string> ans;
    while(!q.empty()){
        string temp = q.top();
        q.pop();
        ans.push_back(temp);
        unordered_set<string> j=Adj[temp] ,c = Adj[temp];
        for (auto y:j) 
        for(int v=0;v<ans.size();v++) 
        if (y==ans[v]) c.erase(ans[v]);
        if(c.size() > 1) for(int w=0;w<c.size();w++) branches.push(temp);
        Node* itr= head;
        if(head == NULL) {
            Node* tem = new Node();
            tem->name = temp;
            head = tem;
            tail = tem;
            }
        else{
             while (itr->next!=NULL) itr = itr->next;
             Node* newwe = new Node();
             newwe->name = temp;
             itr->next = newwe;
             tail = newwe;
        }
        
        if(temp==end) break;
        int counter=0;
        for(string e: Adj[temp]) {
            counter++;
            bool ch = false;
            for(string k:ans) if (k==e) ch = true;
            if(!ch) q.push(e);
            else if(branches.size()>0 && counter == Adj[temp].size())
            {
                Node* itrr=head;
                while (itrr->name != branches.top()) itrr = itrr->next;
                itrr->next = NULL;
                tail = itrr;
            }
            else if(q.empty() || e == q.top()) head = NULL;
        }
}
}


int main(){
    int H;
    string start,end;
    cin >> H;
    string G;
    cin.ignore();
    map<string, unordered_set<string>> Adj_List;
    for (int i = 0; i < H; i++)
    {
        getline(cin, G);
        split(G," ",Adj_List);
    }
    cin >> start >> end;

    dfs(Adj_List,start, end);
    if (head==NULL) cout << "no route found" << endl;
    else{
        Node* itr = head;
        while (itr!=NULL)
        {
            cout << itr->name << " ";
            itr = itr->next;
        }
        cout << endl;
    }
}