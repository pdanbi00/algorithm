class Solution {
    public String solution(String polynomial) {
        String answer = "";
        String[] arr = polynomial.split(" ");
        int xCnt = 0;
        int cnt = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].contains("x")) {
                if (arr[i].equals("x")) {
                    xCnt += 1;
                } else {
                    xCnt += Integer.parseInt(arr[i].replace("x", ""));
                }
            } else if (!arr[i].equals("+")) {
                cnt += Integer.parseInt(arr[i]);
            }
            
        }
        
        if (xCnt > 0 && cnt > 0) {
            if (xCnt == 1) {
                answer = "x + " + cnt;
            } else {
                answer = xCnt+ "x + " + cnt;
            }
            
        } else if (xCnt > 0 && cnt == 0) {
            if (xCnt == 1) {
                answer = "x";
            } else {
                answer = xCnt+ "x";
            }
        } else {
            answer = cnt + "";
        }
        
        return answer;
    }
}