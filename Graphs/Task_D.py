// Task description: You are given N points, starting point d and destination point v. Then you are given R descriptions of transfers between points, which is a bus shedule. 
// each such string contains departure point, departure time,  destination point and arrival time. 
// You need to compute minimal time to arrive from point d to point v or print -1 if it is impossible.


#include <bits/stdc++.h>
using namespace std;
typedef long  long ll;


ll solve_ege(vector<vector<vector<ll>>> &bus_stops, ll start, ll end){
    vector<ll> min_arr_times(bus_stops.size(), LONG_LONG_MAX);
    min_arr_times[start] = 0;
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<>> q;
    q.push({0, start});

    while (!q.empty()){
        auto current_station = q.top().second;
        q.pop();
        for (auto &row: bus_stops[current_station]){
            ll dep_time = row[0], destination = row[1], arr_time = row[2];
            if (dep_time >= min_arr_times[current_station] && arr_time < min_arr_times[destination]){
                min_arr_times[destination] = arr_time;
                q.push({arr_time, destination});
            }
        }
    }
    if (min_arr_times[end] == LONG_LONG_MAX){
        return -1;
    }
    return min_arr_times[end];
}


int main(){
    ll n, d, v, r;
    cin >> n;
    cin >> d >> v;
    cin >> r;
    vector<vector<vector<ll>>> stations(n+1);

    for (int i = 0; i < r; i++){
        ll start, dep_time, end, arr_time;
        cin >> start >> dep_time >> end >> arr_time;
        stations[start].push_back({dep_time, end, arr_time});
    }


    ll res = solve_ege(stations, d, v);
    cout << res;
    return 0;
}
