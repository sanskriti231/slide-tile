#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> move = {{1,3},{0,2,4},{1,5},{0,4},{3,1,5},{4,2}};
    string goal = "123450";

    bool isSolvable(string state)
    {
        int inversions = 0;
        for(int i = 0; i < 6; i++)
        {
            if(state[i] == '0') continue;
            for(int j = i + 1; j < 6; j++)
            {
                if(state[j] == '0') continue;
                if(state[i] > state[j]) inversions++;
            }
        }
        return (inversions & 1) == 0;
    }

    int bfs(string state, unordered_set<string>& set)
    {
        if(state == goal) return 0;
        queue<pair<string, int>> q;
        q.push({state, 0});
        set.insert(state);

        while(!q.empty())
        {
            auto [front, dist] = q.front();
            q.pop();
            if(front == goal) return dist;
            int idx = front.find('0');
            for(auto x: move[idx])
            {
                string newstate = front;
                swap(newstate[idx], newstate[x]);
                if(set.find(newstate) != set.end()) continue;
                set.insert(newstate);
                q.push({newstate, dist + 1});
            }
        }
        return -1;
    }

    int slidingPuzzle(vector<vector<int>>& board) {
        string state = "";
        for(int i = 0; i < 2; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                state += to_string(board[i][j]);
            }
        }
        if(!isSolvable(state)) return -1;
        unordered_set<string> s = {};
        return bfs(state, s);
    }
};