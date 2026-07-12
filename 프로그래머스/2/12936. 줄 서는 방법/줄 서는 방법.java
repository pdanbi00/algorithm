import java.util.*;
class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        List<Integer> arr = new ArrayList<>();
        long total = 1;
        for (int i = 1; i <= n; i++) {
            arr.add(i);
            total *= i;
        }
        
        k--; // 인덱스 0부터니까
        for (int i = 0; i < n; i++) {
            total /= (n-i);
            int idx = (int) (k/total);
            answer[i] = arr.get(idx);
            arr.remove(idx);
            k %= total;
        }
        
        return answer;
    }
}