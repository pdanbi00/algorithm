import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque<Num> q = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(st.nextToken());
            q.add(new Num(n, i+1));
        }
        ArrayList<Integer> answer = new ArrayList();
        while (!q.isEmpty()) {
            Num cur = q.pollFirst();
            answer.add(cur.idx);
            if (cur.num > 0) {
                int cnt = 1;
                while (cnt < cur.num && !q.isEmpty()) {
                    Num tmp = q.pollFirst();
                    q.addLast(tmp);
                    cnt++;
                }
            } else if (cur.num < 0) {
                int cnt = 0;
                while (cnt < Math.abs(cur.num) && !q.isEmpty()) {
                    Num tmp = q.pollLast();
                    q.addFirst(tmp);
                    cnt++;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < answer.size(); i++) {
            sb.append(answer.get(i)).append(" ");
        }
        System.out.println(sb);

    }

    public static class Num {
        int num;
        int idx;

        public Num(int num, int idx) {
            this.num = num;
            this.idx = idx;
        }
    }
}
