import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    static Map<String, List<String>> info;
    static Set<String> files;
    static int cnt;

    static void findFiles(String start) {
        Queue<String> q = new LinkedList<>();
        q.offer(start);

        while (!q.isEmpty()) {
            String cur = q.poll();
            for (String p : info.get(cur)) {
                if (info.containsKey(p)) {
                    q.add(p);
                } else {
                    files.add(p);
                    cnt++;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        info = new HashMap<>();
        List<String> tmp;

        for (int i = 0; i < N+M; i++) {
            st = new StringTokenizer(br.readLine());
            String P = st.nextToken();
            String F = st.nextToken();
            int C = Integer.parseInt(st.nextToken());

            if (!info.containsKey(P)) {
                info.put(P, new ArrayList<>());
            }

            if (C == 1 && !info.containsKey(F)) {
                info.put(F, new ArrayList<>());
            }

            info.get(P).add(F);

        }

        int Q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Q; i++) {
            files = new HashSet<>();
            cnt = 0;
            String[] path = br.readLine().split("/");
            String last = path[path.length - 1];

            findFiles(last);
            sb.append(files.size() + " " + cnt + "\n");
        }
        System.out.print(sb);

    }
}
