class Solution {
    public int[] solution(String s) {
//         int[] answer;
//         int zero = 0;
//         int cnt = 0;
//         while (!s.equals("1")) {
//             String tmp = "";
//             int c = 0;
//             for (int i = 0; i < s.length(); i++) {
//                 if (s.charAt(i) == '0') {
//                     zero++;
//                 } else {
//                     c++;
//                 }
//             }
            
//             while (c > 0) {
//                 tmp += c % 2;
//                 c /= 2;
//             }
            
//             s = tmp;
//             cnt++;
//         }
//         answer = new int[] {cnt, zero};
//         return answer;
        
        int[] answer = new int[2];

        while (s.length() > 1) {
            int one = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    answer[1]++;
                } else {
                    one++;
                }
            }
            
            s = Integer.toBinaryString(one);
            answer[0]++;
        }
        return answer;
    }
}