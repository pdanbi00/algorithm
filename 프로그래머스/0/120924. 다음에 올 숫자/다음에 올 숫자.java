class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int tmp1 = common[1] - common[0];
        int tmp2 = common[2] - common[1];
        if (tmp1 == tmp2) {
            answer = common[common.length - 1] + tmp1;
        } else {
            int tmp = common[1] / common[0];
            answer = common[common.length - 1] * tmp;
        }
        return answer;
    }
}