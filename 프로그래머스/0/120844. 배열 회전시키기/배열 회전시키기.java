import java.util.ArrayList;
class Solution {
    public int[] solution(int[] numbers, String direction) {
        ArrayList<Integer> arr = new ArrayList<>();
        int N = numbers.length;
        int[] answer = new int[N];
        if (direction.equals("right")) {
            arr.add(numbers[N-1]);
            for (int i = 0; i < N-1; i++) {
                arr.add(numbers[i]);
            }
        } else {
            for (int i = 1; i < N; i++) {
                arr.add(numbers[i]);
            }
            arr.add(numbers[0]);
        }
        
        for (int i = 0; i < N; i++) {
            answer[i] = arr.get(i);
        }
        return answer;
    }
}