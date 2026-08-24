class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        int cnt = 0;
        
        while (num > 0) {
            int tmp = num % 10;
            if (tmp == k) {
                answer = cnt;
            }
            num /= 10;
            cnt++;
        }
        if (answer != -1) {
            answer = cnt - answer;
        }
        return answer;
    }
}