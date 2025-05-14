import java.sql.SQLOutput;
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();

        int q = Integer.parseInt(br.readLine());
        int l = S.length();

        // 누적합 기록을 위한 배열 선언
        int[][] arr = new int[l+1][26];

        arr[1][S.charAt(0)-'a']++;

        for (int i = 1; i < l; i++) {
            int idx = S.charAt(i)-'a';
            arr[i+1][idx]++;
            for (int j = 0; j < 26; j++) {
                arr[i + 1][j] += arr[i][j];
            }
        }

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int target = st.nextToken().charAt(0)-'a';
            int start = Integer.parseInt(st.nextToken())+1;
            int end = Integer.parseInt(st.nextToken())+1;
            sb.append(arr[end][target] - arr[start-1][target]).append("\n");
        }
        System.out.println(sb);

    }
}
