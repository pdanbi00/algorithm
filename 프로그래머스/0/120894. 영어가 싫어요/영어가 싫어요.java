class Solution {
    public long solution(String numbers) {
        long answer = 0;
        int N = numbers.length();
        int idx = 0;
        String tmp = "";
        while (idx < N) {
            answer *= 10;
            if (idx + 2 < N) {
                tmp = numbers.substring(idx, idx+3);
                if (tmp.equals("one")) {
                    answer += 1;
                    idx += 3;
                    continue;
                } else if (tmp.equals("two")) {
                    answer += 2;
                    idx += 3;
                    continue;
                } else if (tmp.equals("six")) {
                    answer += 6;
                    idx += 3;
                    continue;
                }
            }
            
            if (idx + 3 < N) {
                tmp = numbers.substring(idx, idx+4);
                if (tmp.equals("zero")) {
                    answer += 0;
                    idx += 4;
                    continue;
                } else if (tmp.equals("four")) {
                    answer += 4;
                    idx += 4;
                    continue;
                } else if (tmp.equals("five")) {
                    answer += 5;
                    idx += 4;
                    continue;
                } else if (tmp.equals("nine")) {
                    answer += 9;
                    idx += 4;
                    continue;
                }
            }
                
            if (idx + 4 < N) {
                tmp = numbers.substring(idx, idx+5);
                if (tmp.equals("three")) {
                    answer += 3;
                    idx += 5;
                    continue;
                } else if (tmp.equals("seven")) {
                    answer += 7;
                    idx += 5;
                    continue;
                } else if (tmp.equals("eight")) {
                    answer += 8;
                    idx += 5;
                    continue;
                }
            }
        }
        return answer;
    }
}