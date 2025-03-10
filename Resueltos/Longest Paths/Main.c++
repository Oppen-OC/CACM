#include <iostream>
#include <vector>
#include <map>
using namespace std;

int maxLength = 0;
int finalNode = 0;

void explore(map<int, vector<int>>& graph, int s, int length) {
    if (graph.find(s) == graph.end()) {
        if (length > maxLength) {
            maxLength = length;
            finalNode = s;
        }
        return;
    }
    
    for (int x : graph[s]) {
        explore(graph, x, length + 1);
    }
}

map<int, vector<int>> create_graph(vector<pair<int, int>>& edges) {
    map<int, vector<int>> graph;
    for (auto& edge : edges) {
        graph[edge.first].push_back(edge.second);
    }
    return graph;
}

int main() {
    int caseNum = 0;
    while (true) {
        caseNum++;
        maxLength = 0;
        finalNode = 0;
        
        int n;
        cin >> n;
        if (n == 0) return 0;
        
        int s;
        cin >> s;
        
        vector<pair<int, int>> edges;
        while (true) {
            int a, b;
            cin >> a >> b;
            if (a == 0 && b == 0) break;
            edges.emplace_back(a, b);
        }
        
        map<int, vector<int>> graph = create_graph(edges);
        explore(graph, s, 0);
        
        cout << "Case " << caseNum << ": The longest path from " << s 
             << " has length " << maxLength << ", finishing at " << finalNode << "." << endl;
    }
    return 0;
}
