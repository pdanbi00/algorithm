class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0, 0};
        int width = board[0] / 2;
        int height = board[1] / 2;
        for (String input : keyinput) {
            if (input.equals("up") && answer[1] < height) {
                answer[1]++;
            } else if (input.equals("down") && answer[1] > -height) {
                answer[1]--;
            } else if (input.equals("left") && answer[0] > -width) {
                answer[0]--;
            } else if (input.equals("right") && answer[0] < width) {
                answer[0]++;
            }
        }
        return answer;
    }
}