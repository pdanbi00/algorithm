import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        double M = Double.parseDouble(br.readLine());

        // 발전소 좌표 입력
        int[][] power = new int[N][2];
        double[][] connected = new double[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            power[i][0] = Integer.parseInt(st.nextToken());
            power[i][1] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    connected[i][j] = Double.MAX_VALUE;
                }
                connected[i][j] = calDis(power[i][0], power[i][1], power[j][0], power[j][1]);
                if (connected[i][j] > M) {
                    connected[i][j] = Double.MAX_VALUE;
                }
            }
        }

        // 연결된 전선 정보
        int a, b;
        for (int i = 0; i < W; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            connected[a-1][b-1] = 0.0;
            connected[b-1][a-1] = 0.0;
        }

        // 0번 발전소에서 다른 발전소까지 연결하는 데에 필요한 추가 전선 길이 최솟값
        double[] distance = new double[N];
        Arrays.fill(distance, Double.MAX_VALUE);
        distance[0] = 0;

        // 다익스트라로 최단길이 구하기
        PriorityQueue<double[]> pq = new PriorityQueue<>((o1, o2) -> Double.compare(o1[0], o2[0]));
        pq.add(new double[] {0, 0});

        double[] now;
        double l;

        while (!pq.isEmpty()) {
            now = pq.poll();

            if (now[0] > distance[(int) now[1]]) {
                continue;
            }

            for (int i = 0; i < N; i++) {
                if (connected[(int) now[1]][i] == Double.MAX_VALUE) {
                    continue;
                }
                l = now[0] + connected[(int) now[1]][i];
                if (l < distance[i]) {
                    distance[i] = l;
                    pq.add(new double[] {l, i});
                }
            }
        }

        System.out.print((int) (distance[N-1] * 1000));
    }

    static double calDis(int x1, int y1, int x2, int y2) {
        double dx = x2 - x1;
        double dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
    }
}
