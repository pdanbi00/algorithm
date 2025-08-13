import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<String> nums = new ArrayList<>();
        // 숫자 만들기
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                if (i != j) {
                    for (int k = 1; k <= 9; k++) {
                        if (j != k && k != i) {
                            int tmp = i * 100 + j * 10 + k;
                            nums.add(String.valueOf(tmp));
                        }
                    }
                }
            }
        }

        StringTokenizer st;
        int[] numCnt = new int[nums.size()];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String num = st.nextToken();
            int strike = Integer.parseInt(st.nextToken());
            int ball = Integer.parseInt(st.nextToken());

            for (int j = 0; j < nums.size(); j++) {
                String n2 = nums.get(j);
                int s = 0;
                int b = 0;
                for (int k = 0; k < 3; k++) {
                    if (n2.contains(String.valueOf(num.charAt(k)))) {
                        b++;
                    }
                    if (num.charAt(k) == n2.charAt(k)) {
                        s++;
                        b--;
                    }

                }

                if (s == strike && b == ball) {
                    numCnt[j]++;
                }
            }
        }
        int answer = 0;
        for (int i = 0; i < numCnt.length; i++) {
            if (numCnt[i] == N) {
                answer++;
            }
        }
        System.out.println(answer);
    }
}
