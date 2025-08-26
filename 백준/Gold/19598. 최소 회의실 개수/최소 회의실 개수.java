import java.io.*;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Time[] lessons = new Time[N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            lessons[i] = new Time(start, end);
        }
        Arrays.sort(lessons);
        PriorityQueue<Integer> q = new PriorityQueue<>();
        q.add(lessons[0].end);
        int answer = 1;

        for (int i = 1; i < N; i++) {
            if (q.peek() <= lessons[i].start) {
                q.poll();
            }
            q.add(lessons[i].end);
            answer = Math.max(answer, q.size());
        }
        System.out.println(answer);
    }

}
class Time implements Comparable<Time>{
    int start, end;

    public Time(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public int compareTo(Time o) {
        if (this.start == o.start) {
            return this.end-o.end;
        } return this.start-o.start;
    }

}