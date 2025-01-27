class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String ab = String.valueOf(a) + String.valueOf(b);
        int tmp = 2 * a * b;
        if (Integer.parseInt(ab) >= tmp) {
            answer = Integer.parseInt(ab);
        } else {
            answer = tmp;
        }
        return answer;
    }
}