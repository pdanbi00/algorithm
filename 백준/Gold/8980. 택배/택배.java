import java.util.*;
import java.io.*;
public class Main {
    public static class Box implements Comparable<Box> {
        int s, e, cnt;

        public Box(int s, int e, int cnt) {
            this.s = s;
            this.e = e;
            this.cnt = cnt;
        }

        public int compareTo(Box o) {
            if (this.e == o.e) {
                return this.s - o.s;
            }
            return this.e - o.e;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(br.readLine());

        ArrayList<Box> box = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int cnt = Integer.parseInt(st.nextToken());

            box.add(new Box(s, e, cnt));
        }

        Collections.sort(box);

        int[] village = new int[N];
        Arrays.fill(village, C);

        int ans = 0;
        for (int i = 0; i < M; i++) {
            Box b = box.get(i);

            // 출발지에서 도착지까지 옮길 수 있는 최대 무게
            int min = C;
            for (int j = b.s; j < b.e; j++) {
                min = Math.min(min, village[j]);
            }

            int tmp = Math.min(b.cnt, min);

            for (int j = b.s; j < b.e; j++) {
                village[j] -= tmp;
            }
            ans += tmp;
        }

        System.out.print(ans);

    }
}
