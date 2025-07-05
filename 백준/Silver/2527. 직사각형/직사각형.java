import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int x3 = Integer.parseInt(st.nextToken());
            int y3 = Integer.parseInt(st.nextToken());
            int x4 = Integer.parseInt(st.nextToken());
            int y4 = Integer.parseInt(st.nextToken());

            System.out.println(check(x1, y1, x2, y2, x3, y3, x4, y4));
        }
    }

    static char check(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
        // 아예 안 만나는 경우
        // 첫번째 정사각형의 위쪽 꼭짓점 보다 두번째 정사각형의 아래쪽 꼭짓점이 높이 있는 경우
        if (y2 < y3 || y4 < y1) {
            return 'd';
        // 첫번째 정사각형의 아래쪽 꼭짓점 보다 두번째 정사각형의 위쪽 꼭짓점이 낮게 있는 경우
        } else if (y1 > y4 || y3 > y2) {
            return 'd';
        // 첫번째 정사각형의 왼쪽 꼭짓점 보다 두번째 정사각형의 오른쪽 꼭짓점이 왼쪽에 있는 경우
        } else if (x1 > x4 || x3 > x2) {
            return 'd';
        // 첫번째 정사각형의 오른쪽 꼭짓점 보다 두번째 정사각형의 왼쪽 꼭짓점이 오른쪽에 있는 경우
        } else if (x2 < x3 || x4 < x1) {
            return 'd';
        }

        // 한 점에서 만나는 경우
        // 첫번째 정사각형의 왼쪽 위 꼭짓점이 두번째 정사각형 오른쪽 아래 꼭짓점과 일치할 경우
        if ((x1 == x4 && y2 == y3) || (x3 == x2 && y4 == y1)) {
            return 'c';
        // 첫번째 정사각형의 오른쪽 위 꼭짓점이 두번째 정사각형 왼쪽 아래 꼭짓점과 일치할 경우
        } else if ((x2 == x3 && y2 == y3) || (x4 == x1 && y4 == y1)) {
            return 'c';
        // 첫번째 정사각형의 왼쪽 아래 꼭짓점이 두번째 정사각형 오른쪽 위 꼭짓점과 일치할 경우
        } else if ((x1 == x4 && y1 == y4) || (x3 == x2 && y3 == y2)) {
            return 'c';
        // 첫번째 정사각형의 오른쪽 아래 꼭짓점이 두번째 정사각형 왼쪽 위 꼭짓점과 일치할 경우
        } else if ((x2 == x3 && y1 == y4) || (x4 == x1 && y3 == y2)) {
            return 'c';
        }

        // 한 변에서 만나는 경우
        // 첫번째 정사각형의 위쪽 변이 두번째 정사각형의 아래쪽 변과 값이 같고 아래쪽 꼭짓점 중 하나가 y, q 사이에 있을 때
        if (y2 == y3 && ((x1 <= x3 && x3 <= x2) || (x1 <= x4 && x4 <= x2) || (x3 <= x1 && x1 <= x4) || (x3 <= x2 && x2 <= x4))) {
            return 'b';
        // 첫번째 정사각형의 아래쪽 변이 두번째 정사각형의 위쪽 변과 값이 같고 위쪽 꼭짓점 중 하나가 y, q 사이에 있을 때
        } else if (y1 == y4 && ((x1 <= x3 && x3 <= x2) || (x1 <= x4 && x4 <= x2) || (x3 <= x1 && x1 <= x4) || (x3 <= x2 && x2 <= x4))) {
            return 'b';
        // 첫번째 정사각형의 왼쪽 변이 두번째 정사각형의 오른쪽 변과 값이 같고 오른쪽 꼭짓점 중 하나가 x, p 사이에 있을 때
        } else if (x1 == x4 && ((y1 <= y4 && y4 <= y2) || (y1 <= y3 && y3 <= y2) || (y3 <= y1 && y1 <= y4) || (y3 <= y2 && y2 <= y4))) {
            return 'b';
        // 첫번째 정사각형의 오른쪽 변이 두번째 정사각형의 왼쪽 변과 값이 같고 오른쪽 꼭짓점 중 하나가 x, p 사이에 있을 때
        } else if (x2 == x3 && ((y1 <= y4 && y4 <= y2) || (y1 <= y3 && y3 <= y2) || (y3 <= y1 && y1 <= y4) || (y3 <= y2 && y2 <= y4))) {
            return 'b';
        }

        return 'a';
    }
}
