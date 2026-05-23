import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(String dirs) {
        Set<String> visited = new HashSet<>();
        
        int curX = 0;
        int curY = 0;
        
        for (int i = 0; i < dirs.length(); i++) {
            int nextX = curX;
            int nextY = curY;
            
            String moving = "";
            
            if (dirs.charAt(i) == 'U') {
                nextY++;
                moving += curX + "" + curY + "->" + nextX + nextY;
            } else if (dirs.charAt(i) == 'D') {
                nextY--;
                moving += nextX + "" + nextY + "->" + curX + curY;
            } else if (dirs.charAt(i) == 'R') {
                nextX++;
                moving += curX + "" + curY + "->" + nextX + nextY;
            } else {
                nextX--;
                moving += nextX + "" + nextY + "->" + curX + curY;
            }
            
            if (nextX < -5 || nextX > 5 || nextY < -5 || nextY > 5) {
                continue;
            }
            visited.add(moving);
            curX = nextX;
            curY = nextY;
        }
        return visited.size();
    }
}