import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] chu = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            chu[i] = Integer.parseInt(st.nextToken());
        }

        boolean[] dp = new boolean[15001];
        for (int c : chu) {
            List<Integer> arr = new ArrayList<>();
            for (int i = 0; i < 15001; i++) {
                if (dp[i]) {
                    arr.add(i);
                }
            }

            for (int i = 0; i < arr.size(); i++) {
                if (arr.get(i) - c >= 0) {
//                    System.out.println(c + " " + (arr.get(i) - c));
                    dp[arr.get(i) - c] = true;
                }

                if (c - arr.get(i) >= 0) {
//                    System.out.println(c + " " + (c - arr.get(i)));
                    dp[c - arr.get(i)] = true;
                }

                if (arr.get(i) + c <= 15000) {
//                    System.out.println(c + " " + (c + arr.get(i)));
                    dp[arr.get(i) + c] = true;
                }
            }

            dp[c] = true;
        }

        int goosle = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < goosle; i++) {
            long num = Long.parseLong(st.nextToken());
            if (num <= 15000) {
                if (dp[(int) num] == true) {
                    System.out.print("Y ");
                } else {
                    System.out.print("N ");
                }
            } else {
                System.out.print("N ");
            }
        }
    }
}
