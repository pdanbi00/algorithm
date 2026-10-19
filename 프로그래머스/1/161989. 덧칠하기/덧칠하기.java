class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        int end = section[0] + m - 1;
        
        for (int point : section) {
            if (point > end) {
                answer++;
                end = point + m - 1;
            }
        }
        return answer;
    }
}