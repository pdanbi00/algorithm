import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Map<Integer, Set<Integer>> dotMap = new HashMap<>();
        Pos[] posArr = new Pos[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            posArr[i] = new Pos(x, y);
            Set<Integer> ySet = dotMap.getOrDefault(x, new HashSet<>());
            ySet.add(y);
            dotMap.put(x, ySet);
        }

        long answer = 0;
        for (int i = 0; i < N-1; i++) {
            int x1 = posArr[i].x;
            int y1 = posArr[i].y;
            for (int j = i+1; j < N; j++) {
                int x2 = posArr[j].x;
                int y2 = posArr[j].y;

                if (x1 == x2 || y1 == y2) {
                    continue;
                }
                if (dotMap.get(x1).contains(y2) && dotMap.get(x2).contains(y1)) {
                    answer++;
                }
            }
        }
        System.out.print(answer/2);
    }

    static class Pos {
        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
