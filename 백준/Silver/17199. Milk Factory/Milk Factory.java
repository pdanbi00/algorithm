import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static ArrayList<ArrayList<Integer>> graph;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(b).add(a);
        }
        boolean find = false;
        int answer = 0;
        for (int i = 1; i <= N; i++) {
            visited = new boolean[N+1];
            visited[0] = true;
            visited[i] = true;
            dfs(i);
            int cnt = 0;
            for (int j = 0; j <= N; j++) {
                if (visited[j]) {
                    cnt++;
                }

            }
            if (cnt == N+1) {
                find = true;
                answer = i;
                break;
            }
        }
        if (find) {
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }


    }
    static void dfs(int now) {
        for (int next : graph.get(now)) {
            if (!visited[next]) {
                visited[next] = true;
                dfs(next);
            }
        }
    }
}
