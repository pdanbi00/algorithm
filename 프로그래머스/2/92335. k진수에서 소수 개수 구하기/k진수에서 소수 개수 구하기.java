class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        // 1. n을 k진수로 변환하기
        String kNum = Integer.toString(n, k);
        String[] arr = kNum.split("0");
        
        // 2. 소수 판별
        for (String s : arr) {
            if (s.equals("")) continue;
            
            long num = Long.parseLong(s);
            if (num == 1) continue;
            if (check(num)) answer++;
        }
        
        return answer;
    }
    static boolean check(long num) {
        long limit = (long) Math.sqrt(num);
        for (long i = 2; i <= limit; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}