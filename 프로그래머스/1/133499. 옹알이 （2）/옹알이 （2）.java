class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] able = {"aya", "ye", "woo", "ma"};
        for (String arr : babbling) {
            if (arr.contains("ayaaya") || arr.contains("yeye") || arr.contains("woowoo") || arr.contains("mama")) {
                continue;
            }
            
            for (String a : able) {
                arr = arr.replace(a, " ");
            }
            arr = arr.replace(" ", "");
            if (arr.length() == 0) answer++;
        }
        return answer;
    }
}