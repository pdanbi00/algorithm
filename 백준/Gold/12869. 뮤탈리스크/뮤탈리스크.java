import java.util.StringTokenizer;
import java.io.*;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    static int N;
    static int[] SVC;
    static int[][] attack = {{9, 3, 1}, {9, 1, 3}, {3, 9, 1}, {3, 1, 9}, {1, 9, 3}, {1, 3, 9}};
    static boolean[][][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        SVC = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            SVC[i] = Integer.parseInt(st.nextToken());
        }
        visited = new boolean[61][61][61];

        System.out.println(bfs(SVC[0], SVC[1], SVC[2]));
    }

    static int bfs(int a, int b, int c) {
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(a, b, c, 0));
        visited[a][b][c] = true;

        while (!q.isEmpty()) {
            Node node = q.poll();
            int na = node.a;
            int nb = node.b;
            int nc = node.c;
            int cnt = node.cnt;

            if (na <= 0 && nb <= 0 && nc <= 0) {
                return cnt;
            }

            for (int k = 0; k < 6; k++) {
                int nna = Math.max(na - attack[k][0], 0);
                int nnb = Math.max(nb - attack[k][1], 0);
                int nnc = Math.max(nc - attack[k][2], 0);

                if (!visited[nna][nnb][nnc]) {
                    visited[nna][nnb][nnc] = true;
                    q.add(new Node(nna, nnb, nnc, cnt+1));
                }
            }
        }
        return -1;
    }

    static class Node {
        int a, b, c, cnt;

        public Node(int a, int b, int c, int cnt) {
            this.a = a;
            this.b = b;
            this.c = c;
            this.cnt = cnt;
        }
    }
}
