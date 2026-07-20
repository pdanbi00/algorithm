import java.util.*;

class Solution {
    static class Node {
        int idx, cost;
        
        Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        // 다익스트라
        // 1번 마을에서 나머지 모든 마을까지의 최단 거리를 계산한 후 거리가 K이하인 곳들 개수 세기
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        int[] distance = new int[N+1];
        
        for (int i = 0; i <= N; i++) {
            ArrayList<Node> arr = new ArrayList<>();
            graph.add(arr);
            distance[i] = Integer.MAX_VALUE;
        }
        
        for (int[] tmp : road) {
            int a = tmp[0];
            int b = tmp[1];
            int c = tmp[2];
            
            graph.get(a).add(new Node(b, c));
            graph.get(b).add(new Node(a, c));
        }
        
        PriorityQueue<Node> q = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost , o2.cost));
        distance[1] = 0;
        q.offer(new Node(1, 0));
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            
            if (distance[cur.idx] < cur.cost) {
                continue;
            }
            
            for (Node next : graph.get(cur.idx)) {
                if (distance[next.idx] > cur.cost + next.cost) {
                    distance[next.idx] = cur.cost + next.cost;
                    q.offer(new Node(next.idx, distance[next.idx]));
                }
            }
        }
        
        for (int i = 1; i <= N; i++) {
            if (distance[i] <= K) {
                answer++;
            }
        }

        return answer;
    }
}