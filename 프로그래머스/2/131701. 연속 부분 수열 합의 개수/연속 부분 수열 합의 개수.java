import java.util.Set;
import java.util.HashSet;
class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        int N = elements.length;
        int[] tmp = new int[N * 2 - 1];
        for (int i = 0; i < N * 2 - 1; i++) {
            tmp[i] = elements[i % N];
        }
        Set<Integer> set = new HashSet<>();
        for (int i = 1; i <= N; i++) {
            int total = 0;
            for (int j = 0; j < i; j++) {
                total += tmp[j];
            }
            set.add(total);
            for (int j = i; j < N * 2 - 1; j++) {
                total += tmp[j];
                total -= tmp[j-i];
                set.add(total);
            }
        }
        
        return set.size();
    }
}