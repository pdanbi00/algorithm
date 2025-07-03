import java.util.*;
import java.io.*;

class Point implements Comparable<Point>{
    int dis;
    int idx;
    public Point(int dis, int idx) {
        this.dis = dis;
        this.idx = idx;
    }

    @Override
    public int compareTo(Point other) {
        return Integer.compare(this.dis, other.dis);
    }

}

public class Main {
    static int T;
    static int n, m, t, s, g, h, a, b, d;
    static ArrayList<ArrayList<Point>> graph;
    static int[] first, gDijk, hDijk;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            g = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            graph = new ArrayList<>();
            for (int i = 0; i < n + 1; i++) {
                ArrayList<Point> arr = new ArrayList<>();
                graph.add(arr);
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                d = Integer.parseInt(st.nextToken());
                graph.get(a).add(new Point(d, b));
                graph.get(b).add(new Point(d, a));
            }

            int[] target = new int[t];
            for (int i = 0; i < t; i++) {
                int tg = Integer.parseInt(br.readLine());
                target[i] = tg;
            }
            first = dijkstra(s);

            gDijk = dijkstra(g);
            hDijk = dijkstra(h);

            ArrayList<Integer> answer = new ArrayList<>();
            for (int tg : target) {
                if (first[g] + gDijk[h] + hDijk[tg] == first[tg] || first[h] + hDijk[g] + gDijk[tg] == first[tg]) {
                    answer.add(tg);
                }
            }

            Collections.sort(answer);
            for (int ans : answer) {
                sb.append(ans + " ");
            }
            sb.append("\n");

        }
        System.out.println(sb);
    }

    static int[] dijkstra(int start) {
        PriorityQueue<Point> q = new PriorityQueue<>();
        int[] distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        q.offer(new Point(0, start));
        distance[start] = 0;
        while (!q.isEmpty()) {
            Point now = q.poll();
            if (now.dis > distance[now.idx]) {
                continue;
            }
            for (Point next : graph.get(now.idx)) {
                int cost = now.dis + next.dis;
                if (cost < distance[next.idx]) {
                    q.add(new Point(cost, next.idx));
                    distance[next.idx] = cost;
                }
            }
        }
        return distance;
    }
}
