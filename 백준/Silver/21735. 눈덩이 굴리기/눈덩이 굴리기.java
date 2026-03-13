import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] yard = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            yard[i] = Integer.parseInt(st.nextToken());
        }

        Queue<int[]> q = new LinkedList<>();
        Set<int[]> set = new HashSet<>();
        q.add(new int[] {0, 0, 1});
        set.add(new int[] {0, 0, 1});
        int answer = 1;

        while (!q.isEmpty()) {
            int[] arr = q.poll();

            int idx = arr[0];
            int time = arr[1];
            int size = arr[2];

            if (time == M || idx >= N) {
                answer = Math.max(answer, size);
                continue;
            }

            // 굴리기
            int nIdx = idx + 1;
            if (nIdx <= N) {
                int nSize = size + yard[nIdx];
                int[] tmp = new int[] {nIdx, time+1, nSize};
                if (!set.contains(tmp)) {
                    q.add(tmp);
                    set.add(tmp);
                }
            }

            // 던지기
            nIdx = idx + 2;
            if (nIdx <= N) {
                int nSize = size / 2 + yard[nIdx];
                int[] tmp = new int[] {nIdx, time+1, nSize};
                if (!set.contains(tmp)) {
                    q.add(tmp);
                    set.add(tmp);
                }
            }
        }
        System.out.print(answer);
    }
}
