class Solution {
public:
    bool hasCycle = false;
    
    void dfs(vector<int>& order, vector<vector<int>>& graph, vector<int>& state, int course) {
        if (hasCycle) return;

        state[course] = 1; // currently visitting

        for (int nextCourse : graph[course]) {
            if (state[nextCourse] == 0) dfs(order, graph, state, nextCourse);
            else if (state[nextCourse] == 1) {
                hasCycle = true;
                return;
            }
        }

        state[course] = 2;
        order.push_back(course);
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for (const auto& p : prerequisites) {
            int a = p[0];
            int b = p[1];
            graph[b].push_back(a);
        }
        vector<int> order;
        vector<int> state(numCourses, 0);

        for (int course = 0; course < numCourses; course++) {
            if (state[course] == 0) {
                dfs(order, graph, state, course);
                if (hasCycle) return {};
            }
        }

        reverse(order.begin(), order.end());
        return order;
    }
};
