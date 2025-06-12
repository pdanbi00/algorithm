import java.util.*;
import java.io.*;
public class Main {
    static int target, a, b;
    static int[] pizzaA, pizzaB, arrA, arrB, sumA, sumB;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        target = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        pizzaA = new int[a * 2 + 1];
        pizzaB = new int[b * 2 + 1];

        for (int i = 1; i <= a; i++) {
            int n = Integer.parseInt(br.readLine());
            pizzaA[i] = n;
            pizzaA[i+a] = n;
        }

        for (int i = 1; i <= b; i++) {
            int n = Integer.parseInt(br.readLine());
            pizzaB[i] = n;
            pizzaB[i+b] = n;
        }

        // 누적함 구하기
        sumA = new int[a * 2 + 1];
        sumA[1] = pizzaA[1];
        for (int i = 2; i <= a*2; i++) {
            sumA[i] = sumA[i-1] + pizzaA[i];
        }

        sumB = new int[b * 2 + 1];
        sumB[1] = pizzaB[1];
        for (int i = 2; i <= b*2; i++) {
            sumB[i] = sumB[i-1] + pizzaB[i];
        }

        arrA = new int[target+1];
        arrB = new int[target+1];
        makeArr(arrA, sumA, a);
        makeArr(arrB, sumB, b);

        int answer = 0;
        // 1. pizza A만 사용하는 경우
        answer += arrA[target];

        // 2. pizza B만 사용하는 경우
        answer += arrB[target];

        // 3. A, B 모두 사용하는 경우
        for (int i = 1; i < target; i++) {
            int j = target-i;
            answer += arrA[i] * arrB[j];
        }
        System.out.println(answer);

    }
    public static void makeArr(int[] arr, int[] sum, int size) {
        for (int i = 1; i < size; i++) { // 몇개의 조각을 선택할 것인지
            for (int s = 1; s <= size; s++) { // 몇번째 조각부터 연속해서 담을건지
                int value = sum[s + i - 1] - sum[s-1];
                if (value > target) {
                    continue;
                }
                arr[value]++;

            }
        }
        // 위에까지는 size-1개의 조각을 선택하는 경우까지만 있기 때문에 모든 조각을 다 선택하는 경우도 고려
        if (sum[size] <= target) {
            arr[sum[size]]++;
        }
    }
}
