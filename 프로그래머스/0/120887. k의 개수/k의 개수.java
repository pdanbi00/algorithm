class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for (int a = i; a <= j; a++) {
            int b = a;
            while (b > 0) {
                int tmp = b % 10;
                if (tmp == k) {
                    answer++;
                }
                b /= 10;
            }
        }
        return answer;
    }
}