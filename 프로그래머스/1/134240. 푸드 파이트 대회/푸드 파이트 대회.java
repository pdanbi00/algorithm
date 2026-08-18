class Solution {
    public String solution(int[] food) {
        String answer = "0";
        int N = food.length;
        
        for (int i = N-1; i > 0; i--) {
            int cnt = food[i];
            if (cnt % 2 == 1) {
                cnt--;
            }
            cnt /= 2;
            
            String tmp = "";
            for (int j = 0; j < cnt; j++) {
                tmp += Integer.toString(i);
            }
            answer = tmp + answer + tmp;
        }
        return answer;
    }
}