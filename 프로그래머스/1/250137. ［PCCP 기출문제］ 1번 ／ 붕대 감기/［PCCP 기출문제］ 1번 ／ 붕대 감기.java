class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int power = health;
        int heal = 0;
        int N = attacks.length;
        int time = 0;
        
        for (int i = 0; i < N; i++) {
            int t = attacks[i][0];
            int attack = attacks[i][1];
            heal += t - 1 - time;
            int tmp = (heal / bandage[0]) * bandage[2] + (heal * bandage[1]);
            
            power = Math.min(health, power + tmp);
            
            time = t;
            power -= attack;
            heal = 0;
            
            if (power <= 0) {
                answer = -1;
                break;
            }
        }
        
        if (answer != -1) {
            answer = power;
        }
        return answer;
    }
}