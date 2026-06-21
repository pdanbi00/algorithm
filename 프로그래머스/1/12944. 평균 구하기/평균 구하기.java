class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int total = 0;
        for (int i : arr) {
            total += i;
        }
        answer = (double) total / arr.length;
        return answer;
    }
}