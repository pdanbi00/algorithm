import java.util.*;

class Solution {
    boolean[] visited;
    ArrayList<String> route;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        int cnt = 0;
        visited = new boolean[tickets.length];
        route = new ArrayList<>();
        
        dfs("ICN", "ICN", tickets, cnt);
        
        Collections.sort(route);
        
        answer = route.get(0).split(" ");
        
        return answer;
    }
    
    public void dfs(String start, String path, String[][] tickets, int cnt) {
        if (cnt == tickets.length) {
            route.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (start.equals(tickets[i][0]) && !visited[i]) {
                visited[i] = true;
                dfs(tickets[i][1], path + " " + tickets[i][1], tickets, cnt+1);
                visited[i] = false;
            }
        }
    }
}