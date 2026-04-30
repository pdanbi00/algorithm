class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        int N = arr.length;
        int max = -987654321;
        int min = 987654321;
        
        for (int i = 0; i < N; i++) {
            int tmp = Integer.parseInt(arr[i]);
            if (tmp > max) {
                max = tmp;
            }
            if (tmp < min) {
                min = tmp;
            }
        }
        answer += String.valueOf(min) + " ";
        answer += String.valueOf(max);
        return answer;
    }
}