import java.util.*;
import java.io.*;

class Coin {
    int value, quantity;
    Coin(int value, int quantity) {
        this.value = value;
        this.quantity = quantity;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 0; t < 3; t++) {
//            boolean[] dp = new boolean[100001];
//            dp[0] = true;
            int sum = 0;
            int N = Integer.parseInt(br.readLine());
            Coin[] coins = new Coin[N+1];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                int coin = Integer.parseInt(st.nextToken());
                int cnt = Integer.parseInt(st.nextToken());
                coins[i+1] = new Coin(coin, cnt);
                sum += coin * cnt;
//                for (int k = 1; k <= cnt; k++) {
//                    dp[k * coin] = true;
//                }
            }
            if (sum % 2 == 1) System.out.println(0);
            else {
                boolean[] dp = new boolean[100001];
                dp[0] = true;
                for (int i = 1; i <= N; i++) {
                    int coin = coins[i].value;
                    int cnt = coins[i].quantity;

                    for (int j = sum/2; j >= coin; j--) {
                        if (dp[j - coin]) {
                            for (int p = 0; p < cnt; p++) {
                                if (j + coin * p <= sum/2){
                                    dp[j + coin * p] = true;
                                }
                                else {
                                    break;
                                }
                            }
                        }
                    }
                }
                if (dp[sum/2]) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            }
        }
    }
}
