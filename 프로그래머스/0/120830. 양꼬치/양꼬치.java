class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int service = n / 10;
        k = k - service;
        if (k < 0) {
            k = 0;
        }
        answer = n * 12000 + k * 2000;
        return answer;
    }
}