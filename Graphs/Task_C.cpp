// This program implements O(E*logV) Dijkstra algorithm

#include <bits/stdc++.h>
using namespace std;

long long dijkstra(vector<vector<pair<long long, long long>>>& adj_list, long long start, long long end) {
    long long n = adj_list.size();
    vector<long long> dist(n, LONG_LONG_MAX);
    dist[start] = 0;

    priority_queue<pair<long long, long long>, vector<pair<long long, long long>>, greater<pair<long long, long long>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        long long u = pq.top().second;
        pq.pop();

        for (auto edge: adj_list[u]) {
            long long v = edge.second;
            long long weight = edge.first;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    if (dist[end] == LONG_LONG_MAX){
        return -1;
    }
    return dist[end];
}


int main(){
    long long n, k, s, f;
    cin >> n >> k;
    vector<vector<pair<long long, long long>>> adj_list(n);
    for (int i = 0; i < k; i++){
        long long start, end, dist;
        cin >> start >> end >> dist;
        start--;
        end--;
        pair<long long, long long> pair1, pair2;
        pair1.first = dist;
        pair2.first = dist;
        pair1.second = end;
        pair2.second = start;
        adj_list[start].push_back(pair1);
        adj_list[end].push_back(pair2);
    }
    cin >> s >> f;
    s--;
    f--;
    long long res = dijkstra(adj_list, s, f);
    cout << res;

    return 0;
}
