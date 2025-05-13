import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;
    static int[] friendMoney;

    public static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    public static void union(int a, int b) {
        int p_a = find(a);
        int p_b = find(b);

        if (friendMoney[p_a] < friendMoney[p_b]) {
            parent[p_b] = p_a;
        } else {
            parent[p_a] = p_b;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        friendMoney = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            friendMoney[i] = Integer.parseInt(st.nextToken());
        }

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            parent[i] = i;
        }

        int ans = 0;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            union(a, b);
        }

        for (int i = 1; i < N+1; i++) {
            if (parent[i] == i) {
                ans += friendMoney[i];
            }
        }

        if (ans <= K) {
            System.out.print(ans);
        } else {
            System.out.print("Oh no");
        }

    }
}
