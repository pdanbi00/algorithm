import java.io.*;
import java.util.StringTokenizer;
public class Main {
    static int[] pre;
    static int[] nxt;
    static int[] stations;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        pre = new int[1000001];
        nxt = new int[1000001];
        stations = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            stations[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            int now = stations[i];
            pre[now] = stations[(i+N-1) % N];
            nxt[now] = stations[(i+1) % N];
        }

        StringBuilder sb = new StringBuilder();
        for (int p = 0; p < M; p++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("BN")) {
                int i = Integer.parseInt(st.nextToken());
                int j = Integer.parseInt(st.nextToken());
                sb.append(String.valueOf(nxt[i])).append("\n");
                insert(i, j);
            } else if (command.equals("BP")) {
                int i = Integer.parseInt(st.nextToken());
                int j = Integer.parseInt(st.nextToken());
                sb.append(String.valueOf(pre[i])).append("\n");
                insert(pre[i], j);
            } else if (command.equals("CN")) {
                int i = Integer.parseInt(st.nextToken());
                sb.append(String.valueOf(nxt[i])).append("\n");
                remove(nxt[i]);
            } else {
                int i = Integer.parseInt(st.nextToken());
                sb.append(String.valueOf(pre[i])).append("\n");
                remove(pre[i]);
            }
        }
        System.out.println(sb);
    }

    // A > B > C -> A > B > D > C
    static void insert(int B, int D) {
        int C = nxt[B];
        nxt[B] = D;
        pre[D] = B;
        nxt[D] = C;
        pre[C] = D;
    }

    // A > B > C -> A  > C
    static void remove(int B) {
        int A = pre[B];
        int C = nxt[B];
        nxt[A] = C;
        pre[C] = A;
    }
}