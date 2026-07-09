// class Solution {
//     public String solution(int n, int t, int m, int p) {
//         String answer = "";
//         String tmp = "";
//         for (int i = 0; i < (m * t); i++) {
//             tmp += Integer.toString(i, n);
//         }

        
//         for (int i = 0; i < t; i++) {
//             char c = tmp.charAt(p-1 + (m*i));
//             if (!Character.isDigit(c)) {
//                 answer += Character.toUpperCase(c);
//             } else {
//                 answer += c;
//             }
//         }
        
//         return answer;
//     }
// }

class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        String tmp = "";
        int num = 0;
        while (tmp.length() < m * t) {
            tmp += Integer.toString(num, n).toUpperCase();
            num++;
        }

        
        for (int i = 0; i < t; i++) {
            answer += tmp.charAt(p-1 + (m*i));
        }
        
        return answer;
    }
}