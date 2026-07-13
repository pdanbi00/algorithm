// 가중치가 단순히 1이기 때문에 다익스트라 안 써도 되고 bfs 하면 됨...
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        int target = 0;
        int[] distance = new int[n+1];
        boolean[] visited = new boolean[n+1];
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < edge.length; i++) {
            int a = edge[i][0];
            int b = edge[i][1];
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = true;
        distance[1] = 0;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (target  < distance[cur]) {
                target = distance[cur];
                answer = 1;
            } else if (target == distance[cur]) {
                answer++;
            }
            
            for (int i = 0; i < graph.get(cur).size(); i++) {
                int b = graph.get(cur).get(i);
                if (!visited[b]) {
                    q.add(b);
                    visited[b] = true;
                    distance[b] = distance[cur] + 1;
                }
            }
        }
        
        return answer;
    }
}