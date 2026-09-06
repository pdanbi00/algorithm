class Solution {
    public int solution(String my_string) {
        int answer = 0;
        int N = my_string.length();
        int idx = 0;
        String num = "";
        while (idx < N) {
            char c = my_string.charAt(idx);
            if (!Character.isDigit(c)) {
                if (num != "") {
                    answer += Integer.parseInt(num);
                }
                num = "";
                idx++;
                continue;
            }
            num += c;
            idx++;
        }
        if (num != "") {
            answer += Integer.parseInt(num);
        }
        return answer;
    }
}