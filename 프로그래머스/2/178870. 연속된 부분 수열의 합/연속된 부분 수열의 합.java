class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[3];
        answer[2] = 1000001;
        int s = 0;
        int e = 0;
        int tmp = sequence[0];
        while (s <= e && e < sequence.length) {
            if (tmp == k) {
                if (e-s+1 < answer[2]) {
                    answer[0] = s;
                    answer[1] = e;
                    answer[2] = e-s+1;
                }
                tmp -= sequence[s];
                s++;
            } else if (tmp > k) {
                tmp -= sequence[s];
                s++;
            } else {
                e++;
                if (e < sequence.length) {
                    tmp += sequence[e];
                }
            }
        }
        int[] result = new int[] {answer[0], answer[1]};
        return result;
    }
}