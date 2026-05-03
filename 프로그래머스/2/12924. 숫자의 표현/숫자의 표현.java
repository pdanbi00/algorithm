class Solution {
    public int solution(int n) {
        int answer = 0;
        int startNum = 1;
        int sum;
        while (startNum <= n) {
            sum = 0;
            for (int i = startNum; i<= n; i++) {
                sum += i;
                if (sum == n) {
                    answer += 1;
                    break;
                } else if (sum > n) {
                    break;
                }
            }
            startNum += 1;
        }
        
        return answer;
    }
}