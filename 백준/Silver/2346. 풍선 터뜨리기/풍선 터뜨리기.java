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
        Deque<Balloon> q = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(st.nextToken());
            q.add(new Balloon(n, i+1));
        }
        ArrayList<Integer> answer = new ArrayList();
        while (!q.isEmpty()) {
            Balloon cur = q.pollFirst();
            answer.add(cur.idx);
            if (cur.num > 0) {
                int cnt = 1;
                while (cnt < cur.num && !q.isEmpty()) {
                    q.addLast(q.pollFirst());
                    cnt++;
                }
            } else if (cur.num < 0) {
                int cnt = 0;
                while (cnt < Math.abs(cur.num) && !q.isEmpty()) {
                    q.addFirst(q.pollLast());
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

}
class Balloon {
    int num;
    int idx;

    public Balloon(int num, int idx) {
        this.num = num;
        this.idx = idx;
    }
}