class Solution {
    public int solution(String my_string) {
        String[] arr = my_string.split(" ");
        int answer = Integer.parseInt(arr[0]);
        int N = arr.length;
        int idx = 1;
        while (idx < N) {
            if (arr[idx].equals("+")) {
                answer += Integer.parseInt(arr[idx+1]);
            } else if (arr[idx].equals("-")) {
                answer -= Integer.parseInt(arr[idx+1]);
            }
            idx++;
        }
        
        return answer;
    }
}