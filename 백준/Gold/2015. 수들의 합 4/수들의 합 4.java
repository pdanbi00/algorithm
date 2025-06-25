// 아이디어
// i부터 j까지의 합은 sum[j] - sum[i-1] = K
// -> sum[j] - K = sum[i-1]
// sum[j] - K의 값이 이전 누적합에 존재한다면 그만큼 갯수 추가
// 이전 누적합과 그것의 개수는 HashMap을 이용해서 저장

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Map<Integer, Integer> map = new HashMap<>();
        int[] numsSum = new int[N+1];

        long answer = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            numsSum[i] = Integer.parseInt(st.nextToken()) + numsSum[i-1];
        }
        map.put(0, 1);
        for (int j = 1; j <= N; j++) {
            answer += map.getOrDefault(numsSum[j] - K, 0);
            map.put(numsSum[j], map.getOrDefault(numsSum[j], 0) + 1);
        }
        System.out.println(answer);
    }
}
