import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(b).add(a);
        }
        boolean[] visited = new boolean[N+1];
        int X = Integer.parseInt(br.readLine());
        Queue<Integer> q = new LinkedList<>();
        visited[X] = true;
        q.add(X);
        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int i = 0; i < graph.get(cur).size(); i++) {
                int next = graph.get(cur).get(i);

                if (!visited[next]) {
                    q.add(next);
                    visited[next] = true;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i <= N; i++) {
            if (visited[i]) {
                ans += 1;
            }
        }
        System.out.print(ans-1);
    }
}
