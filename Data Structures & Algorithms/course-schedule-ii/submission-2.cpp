class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses); //Each graph[i] stores list of courses that depends on course i
        vector<int> indegree(numCourses, 0); //means how many prerequisites course i still has

        for (const auto& p : prerequisites) {
            int a = p[0];
            int b = p[1];
            graph[b].push_back(a);
            indegree[a]++;
        }

        queue<int> q;
        vector<int> order;

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) q.push(i);
        }

        // Start Kahn's algorithm

        while (!q.empty()) {
            int course = q.front();
            q.pop();
            order.push_back(course);

            for (int nextCourse : graph[course]) {
                indegree[nextCourse]--;
                if (indegree[nextCourse] == 0) q.push(nextCourse);
            }
        }

        if ((int)order.size() != numCourses) return {};

        return order;
    }
};
