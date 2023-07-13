#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

const int MAX = 10000;

vector<int> primes;
vector<int> graph[MAX];
bool visited[MAX];

bool isPrime(int num) {
    if (num < 1000 || num > 9999)
        return false;

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return false;
    }

    return true;
}

bool isValidEdge(int num1, int num2) {
    int count = 0;

    while (num1 != 0) {
        if (num1 % 10 != num2 % 10)
            count++;

        num1 /= 10;
        num2 /= 10;
    }

    return count == 1;
}

void buildGraph() {
    for (int i = 1000; i <= 9999; i++) {
        if (isPrime(i))
            primes.push_back(i);
    }

    int n = primes.size();

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int num1 = primes[i];
            int num2 = primes[j];

            if (isValidEdge(num1, num2)) {
                graph[num1].push_back(num2);
                graph[num2].push_back(num1);
            }
        }
    }
}

int bfs(int source, int destination){
    memset(visited, false, sizeof(visited));
    queue<int> q;
    vector<int> dist(MAX, -1);

    q.push(source);
    visited[source] = true;
    dist[source] = 0;

    while (!q.empty())
    {
        int current = q.front();
        q.pop();

        if (current == destination)
            return dist[current];
        
        for (int neighbor : graph[current])
        {
            if (!visited[neighbor]) 
            {
                q.push(neighbor);
                visited[neighbor] = true;
                dist[neighbor] = dist[current] + 1;
            }
        }
    }

    return -1;
}

int main() {
    buildGraph();

    int t;
    cin >> t;

    while (t--) {
        int source, target;
        cin >> source >> target;

        int shortestPath = bfs(source, target);
        cout << shortestPath << endl;
    }

    return 0;
}
