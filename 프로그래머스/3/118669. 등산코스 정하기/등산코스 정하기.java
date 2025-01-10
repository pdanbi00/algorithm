// 다익스트라
// 핵심 : 입구와 산봉우리를 단방향, 쉼터는 양방향 그래프로 만드는 것
// 입구에서 정상까지 가는 경로가 최소이면 돌아오는 경로도 똑같이 최소인 경로로 돌아오면 되므로 입구에서 산봉우리까지 가는 경우의 경로만 생각

// -> 일반적인 다익스트라 코드가 아래라면
// if dist[to] > dist[from] + weight then
//      dist[to] = dist[from] + weight

// if intensity[to] > max(intensity[from], weight) then
//      intensity[to] = max(intensity[from], weight)
// 이렇게 수정

import java.util.*;

class Solution {
    private static List<List<Node>> graph;
    
    private static class Node {
        int e, w; // 노드, 가중치
        
        Node(int e, int w) {
            this.e = e;
            this.w = w;
        }
    }
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        graph = new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] path : paths) {
            int s = path[0];
            int e = path[1];
            int w = path[2];
            
            // 출입구일 경우는 다른 곳으로만 가는 단방향
            // 산봉우리일 경우 특정 한 곳에서 산봉우리로 가는 단방향
            if (isGate(s, gates) || isSummit(e,summits)) {
                graph.get(s).add(new Node(e, w));
            } else if (isGate(e, gates) || isSummit(s, summits)) {
                graph.get(e).add(new Node(s, w));
            } else {
                // 일반 등산로일 경우 양방향
                graph.get(s).add(new Node(e, w));
                graph.get(e).add(new Node(s, w));
            }
            
        }
        // 정상까지 갔을 때 최소이면 같은 경로로 돌아오면 되기 때문에
        // 정상까지 가는 경우만 고려함
        return dijkstra(n, gates, summits);
        
    }
    
    private static int[] dijkstra(int n, int[] gates, int[] summits) {
        Queue<Node> q = new LinkedList<>();
        int[] intensity = new int[n+1];
        
        Arrays.fill(intensity, Integer.MAX_VALUE);
        
        // 출입구 전부 큐에 넣기
        for (int gate : gates) {
            q.add(new Node(gate, 0));
            intensity[gate] = 0; // 시작 지점은 0
        }
        
        while (!q.isEmpty()) {
            Node node = q.poll();
            
            // 현재의 가중치가 저장된 가중치보다 크면 패스
            if (node.w > intensity[node.e]) {
                continue;
            }
            
            for (int i = 0; i < graph.get(node.e).size(); i++) {
                Node next = graph.get(node.e).get(i);
                
                // 최소갱신
                int dis = Math.max(intensity[node.e], next.w);
                if (intensity[next.e] > dis) {
                    intensity[next.e] = dis;
                    q.add(new Node(next.e, dis));
                }
            }
        }
        
        int mountain = Integer.MAX_VALUE; // 산봉우리 번호
        int maxValue = Integer.MAX_VALUE; // 최솟값
        
        // 최솟값이 값으면 산봉우리 번호가 가장 작은 수 출력해야하기 때문에 정렬
        Arrays.sort(summits);
        
        for (int summit : summits) {
            if (intensity[summit] < maxValue) {
                mountain = summit;
                maxValue = intensity[summit];
            }
        }
        
        return new int[]{mountain, maxValue};
        
    }
    
    
    
    // num이 입구인지 확인
    private static boolean isGate(int num, int[] gates) {
        for (int gate : gates) {
            if (num == gate) {
                return true;
            }
        }
        return false;
    }
    
    // num이 산봉우리인지 확인
    private static boolean isSummit(int num, int[] summits) {
        for (int summit : summits) {
            if (num == summit) {
                return true;
            }
        }
        return false;
    }
}