import java.io.*;
import java.util.*;
public class Main {
    static int[] dr = {1, 1, 1, 0, 0, 0, -1, -1, -1};
    static int[] dc = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
    static int R, C;
    static char[][] board;
    static ArrayList<Node> crazy;
    static Node jongsu;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        crazy = new ArrayList<>();

        for (int i = 0; i < R; i++) {
            String arr = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = arr.charAt(j);
                if (board[i][j] == 'R') {
                    crazy.add(new Node(i, j));
                }

                if (board[i][j] == 'I') {
                    jongsu = new Node(i, j);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        String dirs = br.readLine();
        for (int i = 0; i < dirs.length(); i++) {
            int d = dirs.charAt(i) - '0';
            if (!move(d)) {
                System.out.println("kraj " + (i+1));
                return;
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                sb.append(board[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);

    }

    static boolean move(int d) {
        int nr = jongsu.r + dr[d-1];
        int nc = jongsu.c + dc[d-1];

        if (board[nr][nc] == 'R') {
            return false;
        }

        if (board[nr][nc] == '.') {
            jongsu = new Node(nr, nc);
        }

        int[][] visited = new int[R][C];
        ArrayList<Node> removeA =  new ArrayList<>(); // 미친 아두이노가 같은 같에 있는지 확인하기 위해서

        for (Node ardu : crazy) {
            // 8방향 중 가장 가까운 방향 찾기
            int min = Integer.MAX_VALUE;
            int crazyR = 0;
            int crazyC = 0;

            for (int i = 0; i < 9; i++) {
                if (i == 4) {
                    continue;
                }
                int newR = ardu.r + dr[i];
                int newC = ardu.c + dc[i];

                if (0 <= newR && newR < R && 0 <= newC && newC < C) {
                    if (min > Math.abs(newR - jongsu.r) + Math.abs(newC - jongsu.c)) {
                        min = Math.abs(newR - jongsu.r) + Math.abs(newC - jongsu.c);
                        crazyR = newR;
                        crazyC = newC;
                    }
                }
            }
            ardu.r = crazyR;
            ardu.c = crazyC;

            visited[crazyR][crazyC] += 1;
            if (visited[crazyR][crazyC] >= 2) {
                removeA.add(new Node(crazyR, crazyC));
            }
        }

        // 한 칸에 미친 아두이노가 여러개 있다면 다 없애기
        for (int i = 0; i < crazy.size(); i++) {
            if (crazy.get(i).r == jongsu.r && crazy.get(i).c == jongsu.c) {
                return false;
            }

            for (int j = 0; j < removeA.size(); j++) {
                if (crazy.get(i).r == removeA.get(j).r && crazy.get(i).c == removeA.get(j).c) {
                    crazy.remove(i);
                    i--;
                    break;
                }
            }
        }
        draw();
        return true;
    }

    static void draw() {
        for (int i = 0; i < R; i++) {
            Arrays.fill(board[i], '.');
        }
        board[jongsu.r][jongsu.c] = 'I';
        for (Node tmp: crazy) {
            board[tmp.r][tmp.c] = 'R';
        }
    }
}

class Node {
    int r;
    int c;

    Node(int r, int c) {
        this.r = r;
        this.c = c;
    }
}
