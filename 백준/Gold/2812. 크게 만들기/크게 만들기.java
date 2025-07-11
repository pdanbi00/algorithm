import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
public class Main {
     public static void main(String[] args) throws IOException {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(br.readLine());
         int N = Integer.parseInt(st.nextToken());
         int K = Integer.parseInt(st.nextToken());
         String nums = br.readLine();
         Stack<Integer> stack = new Stack<>();
         int idx = 0;
         while (idx < N) {
             while (!stack.isEmpty()) {
                 if (stack.peek() < nums.charAt(idx) - '0') {
                     stack.pop();
                     K--;
                     if (K == 0) {
                         break;
                     }
                 }
                 else {
                     break;
                 }
             }
             if (K == 0) {
                 break;
             }
             stack.push(nums.charAt(idx) - '0');
             idx++;
         }

         while (idx < N) {
             stack.push(nums.charAt(idx) - '0');
             idx++;
         }

         while (K > 0) {
             stack.pop();
             K--;
         }
         StringBuilder sb = new StringBuilder();
         for (int i = 0; i < stack.size(); i++) {
             sb.append(stack.get(i));
         }
         System.out.println(sb);
     }
}
