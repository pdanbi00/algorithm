class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 1;
        for (int i = 2; i <= number; i++) {
            int tmp = 2;
            int num = (int) Math.floor(Math.sqrt(i));
            for (int j = 2; j <= num; j++) {
                if (i % j == 0) {
                    tmp += 2;
                }
            }
            if (num * num == i) {
                tmp -= 1;
            }
            
            if (tmp > limit) {
                answer += power;
            } else {
                answer += tmp;
            }
        }
        return answer;
    }
}