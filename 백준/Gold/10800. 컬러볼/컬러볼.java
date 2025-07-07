import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Ball[] balls = new Ball[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int color = Integer.parseInt(st.nextToken());
            int size = Integer.parseInt(st.nextToken());
            balls[i] = new Ball(size, color, i);
        }
        Arrays.sort(balls);

        int[] answer = new int[N];
        int[] colorCnt = new int[N+1];
        int j = 0;
        int total = 0;
        for (int i = 0; i < N; i++) {
            Ball cur = balls[i];
            while (balls[j].size < cur.size) {
                colorCnt[balls[j].color] += balls[j].size;
                total += balls[j].size;
                j++;
            }
            answer[cur.idx] = total - colorCnt[cur.color];
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(answer[i]).append("\n");
        }
        System.out.println(sb);

    }
    static class Ball implements Comparable<Ball> {
        int size, color, idx;

        public Ball(int size, int color, int idx) {
            this.size = size;
            this.color = color;
            this.idx = idx;
        }

        @Override
        public int compareTo(Ball b) {
            if (this.size == b.size) {
                return this.color - b.color;
            }
            return this.size - b.size;
        }
    }
}
