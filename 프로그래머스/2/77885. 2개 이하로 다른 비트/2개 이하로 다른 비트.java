import java.util.ArrayList;
class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        ArrayList<Long> arr = new ArrayList<>();
        for (int i = 0; i < numbers.length; i++) {
            long num = numbers[i];
            
            if (num % 2 == 0) {
                arr.add(num + 1);
                continue;
            } else {
                long bit = (~num) & (num + 1);
                long target = num + (bit>>1);
                arr.add(target);
            }
        }
        
        for (int i = 0; i < numbers.length; i++) {
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}