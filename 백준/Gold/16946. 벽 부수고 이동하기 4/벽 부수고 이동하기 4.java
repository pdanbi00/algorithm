import java.io.*;
import java.util.*;
public class Main {
    static int N, M;
    static int[][] board;
    static int[][] zero;
    static Map<Integer, Integer> groupSize = new HashMap<>();
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][M];
        zero = new int[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j) - '0';
            }
        }

        // 0 그룹별로 개수 세기
        int groupNum = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0 && zero[i][j] == 0) {
                    bfs(i, j, groupNum++);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0) {
                    sb.append(0);
                } else {
                    Set<Integer> addSet = new HashSet<>();
                    int sum = 1;
                    for (int k = 0; k < 4; k++) {
                        int ni = i + dr[k];
                        int nj = j + dc[k];
                        if (0 <= ni && ni < N && 0 <= nj && nj < M && zero[ni][nj] > 0) {
                            addSet.add(zero[ni][nj]);
                        }
                    }
                    for (int g : addSet) {
                        sum += groupSize.get(g);
                    }
                    sb.append(sum % 10);
                }
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
    static void bfs(int x, int y, int groupNum) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        zero[x][y] = groupNum;
        int count = 1;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (int k = 0; k < 4; k++){
                int nr = now[0] + dr[k];
                int nc = now[1] + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < M && board[nr][nc] == 0 && zero[nr][nc] == 0) {
                    q.offer(new int[]{nr, nc});
                    zero[nr][nc] = groupNum;
                    count++;
                }
            }

        }
        groupSize.put(groupNum, count);
    }
}
