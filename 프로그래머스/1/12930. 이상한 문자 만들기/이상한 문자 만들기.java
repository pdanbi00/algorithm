class Solution {
    public String solution(String s) {
        String answer = "";
        String[] line = s.split(" ", -1);
        int N = line.length;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < line[i].length(); j++) {
                if (j % 2 == 0) {
                    answer += Character.toUpperCase(line[i].charAt(j));
                } else {
                    answer += Character.toLowerCase(line[i].charAt(j));
                }
            }
            if (i < N-1) {
                answer += " ";
            }
        }
        return answer;
    }
}