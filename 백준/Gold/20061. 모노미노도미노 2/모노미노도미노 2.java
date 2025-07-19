import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class Main {
    static int[][] blueBoard;
    static int[][] greenBoard;
    static int score;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 초록색 보드는 행이 타일로 가득 차 있으면 그 행 타일은 모두 사라짐. 그 위에 있던 블록들이 사라진 행 수만큼 아래로 이동
        // 파란색 보드는 열이 타일로 가득차 있으면 그 열 타일 모두 사라짐. 사라진 열의 왼쪽에 있는 블록이 사라진 열 수 만큼 오른쪽으로 이동
        // 한 행이나 열이 사라지면 1점 획득. 즉, 점수는 사라진 행 또는 열의 수와 같음
        // 연한 파란색(파란색 보드의 0열, 1열)에 블록이 있으면 블록이 있는 열 수 만큼 제일 오른쪽 열부터 그 개수만큼 열들에 있는 블록 지움. 그리고 나머지들을 사라진 개수만큼 오른쪽으로 이동시키기
        // 연한 초록색(초록색 보드의 0행, 1행)에 블록이 있으면 블록이 있는 행 수 만큼 제일 아래쪽 행부터 그 개수만큼 행들에 있는 블록 지움. 그리고 나머지들을 사라진 개수만큼 아래쪽으로 이동시키기
        // 행이나 열이 타일로 가득찬 상태랑 연한 칸에 블록 있는 경우가 동시에 발생하면 행이나 열이 타일로 가득찬 경우가 없을때까지 점수 획득하고 나서 연한 칸 과정 처리하기

        // 파란색이랑 초록색을 따로 구분을 해보자!
        blueBoard = new int[4][6];
        greenBoard = new int[6][4];

        score = 0;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            blue(t, x, y);
            green(t, x, y);
        }

        System.out.println(score);
        int cnt = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 4; j++) {
                if (blueBoard[j][i] == 1) {
                    cnt++;
                }

                if (greenBoard[i][j] == 1) {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);



    }
    static void blue(int t, int x, int y) {
        // 1. 블럭 쌓기
        // 블럭 들어오는 행은 고정
        // 열 확인하기
        if (t == 1) { // 1 x 1 블럭일 경우
            int idx = -1;
            for (int j = 0; j < 6; j++) {
                // 채워져 있는 칸 바로 앞에 넣기
                if (blueBoard[x][j] == 1) {
                    idx = j-1;
                    break;
                }
            }
            if (idx == -1) {
                blueBoard[x][5] = 1;
            } else {
                blueBoard[x][idx] = 1;
            }
        } else if (t == 2) { // 1 x 2 블럭일 경우(가로로 긴 경우) (x, y), (x, y+1) 채우기
            int idx = -1;
            for (int j = 0; j < 6; j++) {
                // 채워져 있는 칸 바로 앞에 넣기
                if (blueBoard[x][j] == 1) {
                    idx = j-2;
                    break;
                }
            }
            if (idx == -1) {
                blueBoard[x][5] = 1;
                blueBoard[x][4] = 1;
            } else {
                blueBoard[x][idx] = 1;
                blueBoard[x][idx+1] = 1;
            }
        } else if (t == 3) { // 2 x 1 블럭일 경우(세로로 긴 경우) (x, y), (x+1, y)
            // 두 행 중 먼저 튀어 나온 곳 기준으로
            int idx = -1;
            for (int j = 0; j < 6; j++) {
                // 채워져 있는 칸 바로 앞에 넣기
                if (blueBoard[x][j] == 1 || blueBoard[x+1][j] == 1) {
                    idx = j-1;
                    break;
                }
            }
            if (idx == -1) {
                blueBoard[x][5] = 1;
                blueBoard[x+1][5] = 1;
            } else {
                blueBoard[x][idx] = 1;
                blueBoard[x+1][idx] = 1;
            }
        }

        // 2. 가득찬 열 있는지 확인하기
        ArrayList<Integer> fullCol = new ArrayList<>();
        for (int j = 0; j < 6; j++) {
            int cnt = 0;
            for (int i = 0; i < 4; i++) {
                if (blueBoard[i][j] == 1) {
                    cnt++;
                }
            }
            if (cnt == 4) {
                fullCol.add(j);
                score++;
            }
        }
        if (!fullCol.isEmpty()) {
            // 해당 열들 다 빈칸으로 만들기
            for (int j = 0; j < fullCol.size(); j++) {
                for (int i = 0; i < 4; i++) {
                    blueBoard[i][fullCol.get(j)] = 0;
                }
            }
            // 해당 열들 왼쪽에 있는 블럭들 가득찼던 열 개수만큼 오른쪽으로 옮기기
            int idx = fullCol.get(0); // 이게 가장 왼쪽에 위치한 열이니깐 이 열보다 앞에 있는 열들 옮겨주기
            for (int j = idx-1; j >= 0; j--) {
                for (int i = 0; i < 4; i++) {
                    blueBoard[i][j+fullCol.size()] = blueBoard[i][j];
                    blueBoard[i][j] = 0;
                }
            }
        }

        // 3. 0열 혹은 1열에 블럭 있는지 확인하기
        ArrayList<Integer> zeroCol = new ArrayList<>();
        for (int j = 0; j < 2; j++) {
            int cnt = 0;
            for (int i = 0; i < 4; i++) {
                if (blueBoard[i][j] == 1) {
                    zeroCol.add(j);
                    cnt++;
                    break;
                }
            }
        }
        if (!zeroCol.isEmpty()) {
            // 0열 혹은 1열 중에 블럭 있는 열 개수 만큼 오른쪽부터 없애기
            for (int k = 0; k < zeroCol.size(); k++) {
                for (int i = 0; i < 4; i++) {
                    blueBoard[i][5-k] = 0;
                }
            }
            // 나머지 열들 없앤 열 수 만큼 오른쪽으로 옮기기
            for (int j = 5-zeroCol.size(); j >= 0; j--) {
                for (int i = 0; i < 4; i++) {
                    blueBoard[i][j+zeroCol.size()] = blueBoard[i][j];
                    blueBoard[i][j] = 0;
                }
            }
            // 0열 혹은 1열 블럭 빈칸으로 만들기
            for (int k = 0; k < zeroCol.size(); k++) {
                for (int i = 0; i < 4; i++) {
                    blueBoard[i][1-k] = 0;
                }
            }
        }
    }

    static void green(int t, int x, int y) {
        // 1. 블럭 쌓기
        // 블럭 들어오는 열은 고정
        // 행 확인하기
        if (t == 1) { // 1 x 1 블럭일 경우
            int idx = -1;
            for (int i = 0; i < 6; i++) {
                // 채워져 있는 칸 바로 앞에 넣기
                if (greenBoard[i][y] == 1) {
                    idx = i-1;
                    break;
                }
            }
            if (idx == -1) {
                greenBoard[5][y] = 1;
            } else {
                greenBoard[idx][y] = 1;
            }
        } else if (t == 2) { // 1 x 2 블럭일 경우(가로로 긴 경우) (x, y), (x, y+1) 채우기
            // 두 열 중 먼저 튀어 나온 곳 기준으로
            int idx = -1;
            for (int i = 0; i < 6; i++) {
                // 채워져 있는 칸 바로 앞에 넣기
                if (greenBoard[i][y] == 1 || greenBoard[i][y+1] == 1) {
                    idx = i-1;
                    break;
                }
            }
            if (idx == -1) {
                greenBoard[5][y] = 1;
                greenBoard[5][y+1] = 1;
            } else {
                greenBoard[idx][y] = 1;
                greenBoard[idx][y+1] = 1;
            }
        } else if (t == 3) { // 2 x 1 블럭일 경우(세로로 긴 경우) (x, y), (x+1, y)
            int idx = -1;
            for (int i = 0; i < 6; i++) {
                // 채워져 있는 칸 바로 앞에 넣기
                if (greenBoard[i][y] == 1) {
                    idx = i-2;
                    break;
                }
            }
            if (idx == -1) {
                greenBoard[5][y] = 1;
                greenBoard[4][y] = 1;
            } else {
                greenBoard[idx][y] = 1;
                greenBoard[idx+1][y] = 1;
            }
        }

        // 2. 가득찬 행 있는지 확인하기
        ArrayList<Integer> fullRow = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            int cnt = 0;
            for (int j = 0; j < 4; j++) {
                if (greenBoard[i][j] == 1) {
                    cnt++;
                }
            }
            if (cnt == 4) {
                fullRow.add(i);
                score++;
            }
        }
        if (!fullRow.isEmpty()) {
            // 해당 행들 다 빈칸으로 만들기
            for (int i = 0; i < fullRow.size(); i++) {
                for (int j = 0; j < 4; j++) {
                    greenBoard[fullRow.get(i)][j] = 0;
                }
            }
            // 해당 행들 위쪽에 있는 블럭들 가득찼던 행 개수만큼 아래쪽으로 옮기기
            int idx = fullRow.get(0); // 이게 가장 위쪽에 위치한 행이니깐 이 행보다 위에 있는 열들 옮겨주기
            for (int i = idx-1; i >= 0; i--) {
                for (int j = 0; j < 4; j++) {
                    greenBoard[i+fullRow.size()][j] = greenBoard[i][j];
                    greenBoard[i][j] = 0;
                }
            }
        }

        // 3. 0행 혹은 1행에 블럭 있는지 확인하기
        ArrayList<Integer> zeroRow = new ArrayList<>();
        for (int i = 0; i < 2; i++) {
            int cnt = 0;
            for (int j = 0; j < 4; j++) {
                if (greenBoard[i][j] == 1) {
                    zeroRow.add(i);
                    cnt++;
                    break;
                }
            }
        }
        if (!zeroRow.isEmpty()) {
            // 0행 혹은 1행 중에 블럭 있는 행 개수 만큼 아래쪽부터 없애기
            for (int k = 0; k < zeroRow.size(); k++) {
                for (int j = 0; j < 4; j++) {
                    greenBoard[5-k][j] = 0;
                }
            }
            // 나머지 행들 없앤 행 수 만큼 아래쪽으로 옮기기
            for (int i = 5-zeroRow.size(); i >= 0; i--) {
                for (int j = 0; j < 4; j++) {
                    greenBoard[i+zeroRow.size()][j] = greenBoard[i][j];
                    greenBoard[i][j] = 0;
                }
            }
            // 0행 혹은 1행 블럭 빈칸으로 만들기
            for (int k = 0; k < zeroRow.size(); k++) {
                for (int j = 0; j < 4; j++) {
                    greenBoard[1-k][j] = 0;
                }
            }
        }

    }
}


