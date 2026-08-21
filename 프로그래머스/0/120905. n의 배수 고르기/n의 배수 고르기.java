import java.util.ArrayList;
class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] answer = {};
        ArrayList<Integer> tmp = new ArrayList<>();
        for (int num : numlist) {
            if (num % n == 0){
                tmp.add(num);
            }
        }
        
        answer = new int[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
        return answer;
    }
}