import java.util.*;
import java.io.*;
public class Main {
    static int N;
    static int[] DP;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] relation;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        DP = new int[N];
        graph = new ArrayList<>();
        relation = new int[N];
        for (int i = 0; i < N; i++) {
            ArrayList<Integer> arr = new ArrayList<>();
            graph.add(arr);
        }

        for (int i = 0; i < N; i++) {
            int idx = Integer.parseInt(st.nextToken());
            relation[i] = idx;
            if (i != 0) {
                graph.get(idx).add(i);
            }
        }

        dfs(0);
        System.out.println(DP[0]);
    }

    static void dfs(int node) {
        ArrayList<Integer> node_to_sub = new ArrayList<>();
        for (int sub : graph.get(node)) {
            dfs(sub);
            node_to_sub.add(DP[sub]);
        }

        if (!node_to_sub.isEmpty()) {
            Collections.sort(node_to_sub, Collections.reverseOrder());
            ArrayList<Integer> choose_large_time = new ArrayList<>();
            int max_time = 0;
            for (int i = 0; i < node_to_sub.size(); i++) {
                int tmp = node_to_sub.get(i) + i + 1;
                choose_large_time.add(tmp);
                max_time = Math.max(max_time, tmp);
            }
            DP[node] = max_time;
        }
    }
}
