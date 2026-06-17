// class Solution {
//     public int[] solution(long n) {
//         String nStr = Long.toString(n);
//         int l = nStr.length();
//         int[] answer = new int[l];
//         for (int i = 0; i < l; i++) {
//             answer[i] = Character.getNumericValue(nStr.charAt(l-1-i));
//         }
//         return answer;
//     }
// }

class Solution {
    public int[] solution(long n) {
        int idx = 0;
        int[] answer = new int[Long.toString(n).length()];
        while (n > 0) {
            answer[idx] = (int) (n % 10);
            n /= 10;
            idx++;
        }
        return answer;
    }
}